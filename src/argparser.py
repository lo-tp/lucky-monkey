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
    help='use this argument to input the tushare token,',
    required=True
)

arg_parser.add_argument(
    '--verbosity',
    '-v',
    help='set the logging level, the higher the level, the more info you get',
    type=int,
    choices=range(0, 5),
    default=3
)
