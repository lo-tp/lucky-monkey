from argparser import arg_parser
from network import main as network_main
import logging


def main():
    args = arg_parser.parse_args()
    verbosities = [logging.CRITICAL, logging.ERROR,
                   logging.WARNING, logging.INFO, logging.DEBUG]
    logging.basicConfig(
        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',  # noqa: E501
        datefmt='%Y-%m-%d:%H:%M:%S',
        level=verbosities[args.verbosity]
    )

    logging.debug('token is {}'.format(args.token))
    if args.command == 'network':
        network_main()


if __name__ == '__main__':
    main()
