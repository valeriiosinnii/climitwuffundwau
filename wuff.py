import argparse

from wuff_find import search
from wuff_create import create_new_dog
from wuff_stats import stats


def run(args):
    if args.find:
        search(args.find)
    elif args.create:
        if args.output:
            create_new_dog(output=args.output)
        else:
            create_new_dog(output='C:\\Users\\Public')
    elif args.stats:
        stats()


def get_parser():
    parser = argparse.ArgumentParser(description='Providing information about dogs in Zurich')
    parser.add_argument('stats', help='Stats about dogs', action='store_true')
    parser.add_argument('-f', '--find', help='Search for dogs')
    parser.add_argument('-c', '--create', help='Create a new dog', action='store_true')
    parser.add_argument('-o', '--output', help='Output directory')

    return parser


def main(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


main()
