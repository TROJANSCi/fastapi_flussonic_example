from os.path import dirname, join
from typing import Union

import hjson

SETTINGS = join(dirname(dirname(__file__)), 'settings.hjson')


def get_setting(key: str = None) -> Union[str, int, None]:
    try:
        with open(SETTINGS, 'rb') as set_file:
            return hjson.load(set_file, encoding='utf-8').get(key)
    finally:
        set_file.close()
