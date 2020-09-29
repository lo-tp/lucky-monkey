import requests
from sys import argv
from json import dumps


class TushareError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


def sendRequest(arg):
    response = requests.post(
        "http://api.waditu.com",
        data=dumps(arg))
    response.raise_for_status()
    data = response.json()
    if data['code']:
        raise TushareError(data['code'], data['msg'])
    return response.json()


if __name__ == "__main__":
    data = {
        "api_name": "daily",
        "token": argv[1],
        "params": {
            "ts_code": "000001.SZ",
            "start_date": 20181010,
            "end_date": 20181020
        },
        "fields": "ts_code, trade_date, open"
    }
    print(sendRequest(data))
