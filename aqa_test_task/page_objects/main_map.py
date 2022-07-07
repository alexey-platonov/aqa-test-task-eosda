from __future__ import annotations

from selene import have
from selene.support.shared import browser


class MainMap:
    def __init__(self):
        self._url = '/main-map/fields/all'

    def should_be_opened(self) -> MainMap:
        browser.should(have.url(browser.config.base_url + self._url))
        return self
