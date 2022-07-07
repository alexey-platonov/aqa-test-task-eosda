from aqa_test_task import app, api
from aqa_test_task.models import User
from aqa_test_task.utils import fake
from aqa_test_task.utils.one_sec_mail import OneSecMailBox


def test_registration():
    mailbox = OneSecMailBox()

    app.registration_form\
        .open()\
        .should_be_opened()

    app.registration_form\
        .fill_in_first_name_input(fake.first_name())\
        .fill_in_last_name_input(fake.last_name())\
        .fill_in_email_input(mailbox.email)\
        .fill_in_password_input(fake.password())\
        .click_policy_checkbox()\
        .email_input_should_pass_validation_check()\
        .submit()

    app.confirm_email_form.should_be_opened()

    messages_list = mailbox.wait_for_messages()
    message = mailbox.message(messages_list[0]['id'])

    app.confirm_email_form.fill_in_confirm_code_input(message.get_confirmation_code())

    app.main_map.should_be_opened()


def test_login():
    # prepare user (precondition)
    mailbox = OneSecMailBox()

    user = User(
        email=mailbox.email,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        password=fake.password()
    )

    response = api.auth.register(user)
    assert response.status_code == 201

    messages_list = mailbox.wait_for_messages()
    message = mailbox.message(messages_list[0]['id'])

    response = api.auth.confirm_email_with_code(user.email, message.get_confirmation_code())
    assert response.status_code == 200

    # test
    app.login_form\
        .open()\
        .should_be_opened()

    app.login_form\
        .fill_in_email_input(user.email)\
        .fill_in_password_input(user.password)\
        .submit()

    app.main_map.should_be_opened()
