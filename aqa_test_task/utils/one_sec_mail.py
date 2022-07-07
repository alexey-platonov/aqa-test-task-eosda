import time
from datetime import datetime, timedelta

import pytz
import requests
from bs4 import BeautifulSoup

from tests import LOGGER


class OneSecMailBox:
    def __init__(self, timeout_seconds: int = 60):
        self.base_url = 'https://www.1secmail.com/api/v1/'
        self.email = self.get_random_mailbox()
        self.timeout_seconds = timeout_seconds

    def get_random_mailbox(self):
        params = {
            'action': 'genRandomMailbox',
            'count': 1
        }

        return requests.get(self.base_url, params=params).json()[0]

    def get_messages_list(self):
        params = {
            'action': 'getMessages',
            'login': self.email.split('@')[0],
            'domain': self.email.split('@')[1]
        }

        return requests.get(self.base_url, params=params).json()

    def wait_for_messages(self):
        LOGGER.info(f'Waiting for message. Waiting time is {self.timeout_seconds} seconds')
        start_datetime = datetime.now()
        while (datetime.now() - start_datetime) < timedelta(seconds=self.timeout_seconds):
            messages_list = self.get_messages_list()
            if messages_list:
                LOGGER.info('Email is found')
                return messages_list
            else:
                time.sleep(5)
                LOGGER.info('Waiting...')
        raise AssertionError(f'Can not find emails with timeout={self.timeout_seconds}')

    def message(self, message_id):
        return OneSecMessage(message_id, self)


class OneSecMessage:
    def __init__(self, message_id: int, mailbox: OneSecMailBox):
        self.id: int = message_id
        self.mailbox: OneSecMailBox = mailbox
        self.message_obj = self.get_message_by_id(message_id)
        self.sender: str = self.message_obj['from']
        self.subject: str = self.message_obj['subject']
        self.date: datetime = datetime.strptime(self.message_obj['date'] + '+0200', '%Y-%m-%d %H:%M:%S%z')\
            .astimezone(pytz.utc)
        self.attachments: list = self.message_obj['attachments']
        self.body: str = self.message_obj['body']
        self.text_body: str = self.message_obj['textBody']
        self.html_body: str = self.message_obj['htmlBody']

        self._confirmation_code_selector = 'div[style*="display: table;"] span'

    def get_message_by_id(self, message_id: int):
        params = {
            'action': 'readMessage',
            'login': self.mailbox.email.split('@')[0],
            'domain': self.mailbox.email.split('@')[1],
            'id': message_id
        }

        return requests.get(self.mailbox.base_url, params=params).json()

    def get_confirmation_code(self) -> str:
        parsed_html = BeautifulSoup(self.html_body, features="html.parser")
        return parsed_html.select_one(self._confirmation_code_selector).text.replace('-', '')
