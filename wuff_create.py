import random
import requests
import pathlib
import os
import csv

URL = 'https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv'


def read_data():
    try:
        response = requests.get(URL)
        response.encoding = "utf-8-sig"
        lines = response.text.splitlines()
        return csv.DictReader(lines)
    except Exception as e:
        return e


def create_new_dog(output):
    name = create_new_dog_name()
    birth_year = create_new_dog_years()
    sex = create_new_dog_sexes()
    output_file = download_dog_image(output)
    print("Here's your new dog!")
    print(f'Name:{name}')
    print(f'Birth year:{birth_year}')
    print(f'Sex:{sex}')
    print(f'The image of the new dog can be found here: {output_file}')


def create_new_dog_name():
    dogs = read_data()
    name = random.choice([dog['HundenameText'] for dog in dogs])
    return name


def create_new_dog_years():
    dogs = read_data()
    birth_year = random.choice([year['GebDatHundJahr'] for year in dogs])
    return birth_year


def create_new_dog_sexes():
    dogs = read_data()
    sex = random.choice([year['SexHundLang'] for year in dogs])
    return sex


def download_dog_image(output_dir='/Users/rev4l/'):
    response = requests.get('https://random.dog/woof.json')
    response_json = response.json()
    media_url = response_json['url']
    file_name = f'{create_new_dog_name()}_{create_new_dog_years()}{pathlib.Path(media_url).suffix}'
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'wb') as f:
        response = requests.get(media_url, stream=True)
        for chunk in response.iter_content():
            f.write(chunk)
    return f'{output_dir}{file_name}'
