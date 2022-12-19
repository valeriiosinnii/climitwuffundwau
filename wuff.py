import csv
import requests
import argparse
import random
import pathlib
import os
from collections import Counter
from wuff-create


URL = 'https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv'


def read_data():
    try:
        response = requests.get(URL)
        response.encoding = "utf-8-sig"
        lines = response.text.splitlines()
        return csv.DictReader(lines)
    except Exception as e:
        return e


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
