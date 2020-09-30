import argparse

arg_parser = argparse.ArgumentParser(
    description='This is a script used to get stock datas')

arg_parser.add_argument(
    "command",
    help="what command do you want to do",
)

arg_parser.add_argument(
    '--token',
    '-t',
    help='use this argument to input the tushare token',
    required=True
)
