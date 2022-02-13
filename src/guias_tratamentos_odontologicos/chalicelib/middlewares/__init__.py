import builtins
import os
from typing import Union

import requests
from requests import Response


def get_infos(
        path: builtins.str,
        query: builtins.str = None,
        value: Union[builtins.str, builtins.int] = None
) -> Response:

    if query and value:
        info = requests.get(
            f'{os.environ["SERVER"]}/{path}?'
            f'{query}={value}'
        )
    else:
        info = requests.get(
            f'{os.environ["SERVER"]}/{path}'
        )
    return info