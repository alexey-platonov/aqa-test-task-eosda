from __future__ import annotations

from selene import be, have
from selene.support.shared import browser


class RegistrationForm:
    def __init__(self):
        self._url = '/login'
        self._form = browser.element('[data-id=registration-form]')
        self._first_name_input = self._form.element('[data-id=first_name]')
        self._last_name_input = self._form.element('[data-id=last_name]')
        self._email_input = self._form.element('[data-id=email]')
        self._password_input = self._form.element('[data-id=password]')
        self._policy_confirm_checkbox = self._form.element('[data-id=policy_confirm]')
        self._submit_button = self._form.element('[data-id=sign-up-btn]')

    def open(self) -> RegistrationForm:
        browser.open(self._url)
        return self

    def should_be_opened(self) -> RegistrationForm:
        self._form.should(be.visible)
        return self

    def fill_in_first_name_input(self, value: str) -> RegistrationForm:
        self._first_name_input.type(value)
        return self

    def fill_in_last_name_input(self, value: str) -> RegistrationForm:
        self._last_name_input.type(value)
        return self

    def fill_in_email_input(self, value: str) -> RegistrationForm:
        self._email_input.type(value)
        return self

    def fill_in_password_input(self, value: str) -> RegistrationForm:
        self._password_input.type(value)
        return self

    def email_input_should_pass_validation_check(self) -> RegistrationForm:
        self._email_input.should(have.css_class('ng-valid'))
        return self

    def click_policy_checkbox(self) -> RegistrationForm:
        self._policy_confirm_checkbox.click()
        return self

    def submit(self):
        self._submit_button.click()


class ConfirmEmailForm:
    def __init__(self):
        self._form = browser.element('.resend-form')
        self._confirm_code_input = self._form.element('[data-id=confirm-code-input]')
        self._submit_button = self._form.element('[data-id=submit-code-btn]')

    def should_be_opened(self) -> ConfirmEmailForm:
        self._form.should(be.visible)
        return self

    def fill_in_confirm_code_input(self, value: str) -> ConfirmEmailForm:
        self._confirm_code_input.type(value)
        return self

    def submit(self):
        self._submit_button.click()


class LoginForm:
    def __init__(self):
        self._url = '/login/auth'
        self._form = browser.element('[data-id=login-form]')
        self._email_input = self._form.element('[data-id=email]')
        self._password_input = self._form.element('[data-id=password]')
        self._submit_button = self._form.element('[data-id=sign-in-btn]')

    def open(self) -> LoginForm:
        browser.open(self._url)
        return self

    def should_be_opened(self) -> LoginForm:
        self._form.should(be.visible)
        return self

    def fill_in_email_input(self, value: str) -> LoginForm:
        self._email_input.type(value)
        return self

    def fill_in_password_input(self, value: str) -> LoginForm:
        self._password_input.type(value)
        return self

    def submit(self):
        self._submit_button.click()
