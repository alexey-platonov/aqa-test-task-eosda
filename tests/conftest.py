import pytest
from selene.support.shared import browser

from tests.config import settings


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = settings.base_url_ui
    browser.config.timeout = 10
    yield
    browser.quit()
