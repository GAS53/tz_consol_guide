from pathlib import Path
import settings


def print_val_row():
    '''распечатка пронумерованного списка'''
    for num, i in enumerate(settings.ROW_PARAMS):
        print(f'{num} - {i}')


def check_db():
    '''проверка и создание если не существует файла базы'''
    if not Path(settings.DB_PATH).exists():
        Path(settings.DB_PATH).mkdir()
    if not Path(settings.DB_FILE).exists():
        Path(settings.DB_FILE).touch()


def clean_rows(li: list):
    '''очистка строк таблици для вывода'''
    return [i.replace('\n', '') for i in li]


def get_rows():
    '''получение строк из файла'''
    with open(settings.DB_FILE, 'r') as file:
        rows = file.readlines()
    return clean_rows(rows)


def get_preparated_rows():
    '''подготовка строк для поиска'''
    li = get_rows()
    return [i.split(settings.ROW_SEPARATOR) for i in li]


def pprint_list(li: list, easy_li: bool):
    '''показать строки с нумерацией и без'''
    for i in li:
        if easy_li:
            print(i)
        else:
            if i:
                print(f'{i[0]}) {i[1]}')


def set_new_row():
    '''получение новой строки'''
    result_row = ''
    for val_name in settings.ROW_PARAMS:
        if result_row != '':
            result_row += settings.ROW_SEPARATOR
        val = input(f'введите - {val_name}: ')
        result_row += val
    return result_row