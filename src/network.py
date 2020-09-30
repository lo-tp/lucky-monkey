import requests
from json import dumps
from argparser import arg_parser
from logging import debug, error, info


class TushareError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return '{}:{}'.format(self.code, self.message)


def sendRequest(arg):
    debug('send request with following args: {}'.format(arg))
    response = requests.post(
        "http://api.waditu.com",
        data=dumps(arg))
    response.raise_for_status()
    data = response.json()
    debug('response: {}'.format(data))

    if data['code']:
        raise TushareError(data['code'], data['msg'])
    return data


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
        info(sendRequest(data))
    except TushareError as tushareError:
        error("something went wrong with the tushare part")
        debug("Tushare Error: {}".format(tushareError))
