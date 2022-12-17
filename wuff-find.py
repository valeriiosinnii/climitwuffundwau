from wuff import read_data


def search(name, year=None):
    dogs = read_data()

    if year is not None:
        dogs = [dog for dog in dogs if dog['StichtagDatJahr'] == year]

    dogs = [dog for dog in dogs if dog['HundenameText'].lower() == name.lower()]

    print(f'Found {len(dogs)} dogs with the name "{name}":')
    for dog in dogs:
        print(f' - {dog["HundenameText"]} ({dog["SexHundLang"]}, born in {dog["StichtagDatJahr"]})')

