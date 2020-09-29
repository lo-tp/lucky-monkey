import requests
from sys import argv
from json import dumps
import argparse


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
    parser = argparse.ArgumentParser(description='This is the network module')
    parser.add_argument(
        '--token',
        help='use this argument to input the tushare token',
        required=True
    )
    args = parser.parse_args()
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
