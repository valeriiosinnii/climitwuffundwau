import argparse
from wuff_find import search
from wuff_create import create_new_dog
from wuff_stats import stats

def run(args):
    if args.find:
        search(args.find)
    elif args.create:
        if args.outputdir:
            create_new_dog(output=args.outputdir)
        else:
            create_new_dog(output='/Users/rev4l/')
    elif args.stats:
        stats()


def get_parser():
    parser = argparse.ArgumentParser(description='Dog data around Zurich')
    parser.add_argument('find', help='Search for dogs', nargs="?")
    parser.add_argument('stats', help='Stats about dogs', action='store_true')
    parser.add_argument('--create', help='Create a new dog', action='store_true')
    parser.add_argument('--outputdir', '-o', help='Output directory(With --create usage only)', nargs="?")
    return parser


def main(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


main()
