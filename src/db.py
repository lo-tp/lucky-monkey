import psycopg2
import argparse
from argparser import arg_parser as shared_arg_parser


def initilize(database, user, host, port, password):
    connection = psycopg2.connect(
        database=database,
        user=user,
        host=host,
        port=port,
        password=password
    )
    cursor = connection.cursor()
    cursor.close()
    connection.close()


def main():
    arg_parser = argparse.ArgumentParser(parents=[shared_arg_parser])
    arg_parser.add_argument(
        '--user',
        '-u',
        help='use this argument to input the postgres db user,',
        required=True
    )

    arg_parser.add_argument(
        '--host',
        help='use this argument to input the postgres db host',
        required=True
    )

    arg_parser.add_argument(
        '--port',
        '-p',
        help='use this argument to input the postgres db port,',
        required=True
    )

    arg_parser.add_argument(
        '--password',
        help='use this argument to input the postgres db password,',
        required=True
    )

    arg_parser.add_argument(
        '--database',
        help='use this argument to input the postgres db name,',
        required=True
    )
    args = arg_parser.parse_args()
    initilize(database=args.database, user=args.user, host=args.host,
              port=args.port, password=args.password)
