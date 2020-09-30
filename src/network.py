import requests
from json import dumps
from argparser import arg_parser


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


def main():
    args = arg_parser.parse_args()
    try:
        data = {
            "api_name": "daily",
            "token": args.token,
            "params": {
                "ts_code": "000001.SZ",
                "start_date": 20181010,
                "end_date": 20181020
            },
            "fields": "ts_code, trade_date, open"
        }
        print(sendRequest(data))
    except TushareError:
        print("something went wrong with the tushare part")
