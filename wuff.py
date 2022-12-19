import csv
import requests
import argparse
from wuff-find import search
from wuff-create import create_new_dog
from wuff-stats import stats

def run(args):
    if args.find:
        search()
    elif args.stats:
        stats()
    elif args.create:
        create_new_dog()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--find', help='finds the dog/dogs')
    parser.add_argument('--create', help='create a new dog')
    parser.add_argument('--stats', help='gives stats')
    parser.add_argument("--year", help="year to use for data analysis")
    return parser


def main(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


main()
