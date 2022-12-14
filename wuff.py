import csv
import requests


URL = 'https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv'


def read_data():
    try:
        # Download the data from the Open Data website
        response = requests.get(URL)
        response.encoding = "utf-8-sig"

        # Split the response into lines and remove the UTF-8 Byte Order Mark
        lines = response.text.splitlines()

        # Parse the CSV data into a list of dictionaries
        return csv.DictReader(lines)
    except Exception as e:
        return e



