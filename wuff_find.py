import csv

import requests
from rich.console import Console
from rich.table import Table

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

    table = Table(title=f'Found {len(dogs)} dogs with the name "{name}":')

    table.add_column("Dogs Name :dog_face-emoji: ", justify="right", style="cyan", no_wrap=True)
    table.add_column("Sex", style="magenta")
    table.add_column("Birth", justify="right", style="green")
    for dog in dogs:
        table.add_row(f' - {dog["HundenameText"]}', f'({dog["SexHundLang"]}',
                      f'born in [italic red]{dog["StichtagDatJahr"]}[/italic red])')

    console = Console()
    console.print(table)
