import requests
from requests.models import Response

from aqa_test_task.models import User
from tests.config import settings


class Auth:
    @staticmethod
    def register(user: User) -> Response:
        url = f'{settings.base_url_api}/service/auth/account/register/'

        payload = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'password': user.password,
            'policy_confirm': True,
            'recaptcha_response': 1111,
            'consent_details': {'policy_consent': [1]}
        }

        return requests.post(url, json=payload)

    @staticmethod
    def confirm_email_with_code(email: str, code: str) -> Response:
        url = f'{settings.base_url_api}/service/auth/account/confirm/email/code/'

        payload = {
            'email': email,
            'code': code
        }

        return requests.post(url, json=payload)
