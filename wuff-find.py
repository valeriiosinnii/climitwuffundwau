from wuff import read_data


def search(name, year=None):
    # Download the data
    dogs = read_data()

    # Filter the data based on the year (if specified)
    if year is not None:
        dogs = [dog for dog in dogs if dog['StichtagDatJahr'] == year]

    # Filter the data based on the name
    dogs = [dog for dog in dogs if dog['HundenameText'].lower() == name.lower()]

    # Print the search results
    print(f'Found {len(dogs)} dogs with the name "{name}":')
    for dog in dogs:
        print(f' - {dog["HundenameText"]} ({dog["SexHundLang"]}, born in {dog["StichtagDatJahr"]})')


search('Aaron', "2015")
