from typing import Literal, Optional

import pydantic

from tests import TESTS_DIR

EnvContext = Literal['test']


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'test'

    base_url_ui: str = ''
    base_url_api: str = ''

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        asked_or_current = env or cls().context
        return cls(_env_file=f'{TESTS_DIR}/config.{asked_or_current}.env')


settings = Settings.in_context()
