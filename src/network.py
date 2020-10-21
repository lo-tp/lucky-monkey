import requests
import argparse
from json import dumps
from argparser import arg_parser as shared_arg_parser
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


def get_company(parent_argparser):
    arg_parser = argparse.ArgumentParser(parents=[parent_argparser])
    arg_parser.add_argument(
        "--code",
        "-c",
        required=True,
        help="what is the code of the company you are interested in",
    )
    arg_parser.add_argument(
        "--fields",
        "-f",
        required=True,
        help="what is the fields you are interested in",
    )
    args = arg_parser.parse_args()
    debug("code: {}".format(args.code))
    debug("fields: {}".format(args.fields))

    res = None
    try:
        data = {
            "api_name": "stock_company",
            "token": args.token,
            "params": {
                "ts_code": args.code
            },
            "fields": args.fields
        }
        res = sendRequest(data)
    except TushareError as tushareError:
        error("something went wrong with the tushare part")
        debug("Tushare Error: {}".format(tushareError))
    return res


def main():
    arg_parser = argparse.ArgumentParser(
        add_help=False,
        parents=[shared_arg_parser])
    arg_parser.add_argument(
        '--token',
        '-t',
        help='use this argument to input the tushare token,',
        required=True
    )
    arg_parser.add_argument(
        "sub_command",
        help="what sub command do you want to use",
    )

    args, _ = arg_parser.parse_known_args()

    debug(args.sub_command)
    debug('token is {}'.format(args.token))

    if args.sub_command == "check_company":
        info(get_company(arg_parser))
