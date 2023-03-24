import json
from pathlib2 import Path

from pic_core.utils.log import getMyLogger


log = getMyLogger(__file__)


def load_json(file_path, encoding='utf-8'):
    """
    Takes json file path, encoding code as parameters, and returns back a JSON object
    :param file_path:
    :param encoding: i.e. utf-8, big5
    :return: JSON object
    """
    if Path(file_path).exists():
        _config_file = str(Path(file_path))
        log.debug(f"Json file located at - {_config_file}")
        log.debug(f"File encoding - {encoding}")
        with open(_config_file, 'r', encoding=encoding, errors='ignore') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as err:
                log.error(f'Json file cotains error - {err}')
                return None
    else:
        log.error(f"file not found at directory - {str(Path(file_path))}")


def load_json_data(data, encoding='utf-8'):
    """
    Takes a json text string, encoding code as parameters, and returns back a JSON object
    :param data:  A JSON text string
    :param encoding: i.e. utf-8, big5
    :return: JSON object
    """
    try:
        return json.loads(data, encoding=encoding)
    except (json.JSONDecodeError, ValueError) as err:
        log.error(f'Error seen at below Json : {data}')
        log.error(f'Error - {err}')
        return None


def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        log.error(f'invalid json found : {data}')
        log.error(f'Value Error - {error}')
        return False
