from pathlib import Path

import settings


def check_db():
    if not Path(settings.DB_PATH).exists():
        Path(settings.DB_PATH).mkdir()
    if not Path(settings.DB_FILE).exists():
        Path(settings.DB_FILE).touch()


def clean_rows(li):
    return [i.replace('\n', '') for i in li]


def get_rows():
    with open(settings.DB_FILE, 'r') as file:
        rows = file.readlines()
    return clean_rows(rows)


def pprint_list(li):
    for i in li:
        if i:
            print(f'{i[0]}) {i[1]}')