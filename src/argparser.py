import argparse

arg_parser = argparse.ArgumentParser(description='This is the network module')
arg_parser.add_argument(
    '--token',
    help='use this argument to input the tushare token',
    required=True
)
