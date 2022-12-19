import csv
import requests

URL = 'https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv'


def read_data():
    try:
        response = requests.get(URL)
        response.encoding = "utf-8-sig"
        lines = response.text.splitlines()
        return csv.DictReader(lines)
    except Exception as e:
        return e


def search(name, year=None):
    dogs = read_data()

    if year is not None:
        dogs = [dog for dog in dogs if dog['StichtagDatJahr'] == year]

    dogs = [dog for dog in dogs if dog['HundenameText'].lower() == name.lower()]

    print(f'Found {len(dogs)} dogs with the name "{name}":')
    for dog in dogs:
        print(f' - {dog["HundenameText"]} ({dog["SexHundLang"]}, born in {dog["StichtagDatJahr"]})')
