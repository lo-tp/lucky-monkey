from argparser import arg_parser
from network import main as network_main


def main():
    args = arg_parser.parse_args()
    if args.command == 'network':
        network_main()


if __name__ == '__main__':
    main()
