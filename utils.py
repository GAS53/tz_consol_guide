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


def set_new_row():
    result_row = ''
    for val_name in settings.ROW_PARAMS:
        if result_row != '':
            result_row += settings.ROW_SEPARATOR
        val = input(f'введите - {val_name}: ')
        result_row += val
    return result_row