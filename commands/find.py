from utils import get_preparated_rows, print_val_row, pprint_list
from settings import ROW_SEPARATOR

def run():
    '''поиск по значениям строк'''
    li = get_preparated_rows()
    finded_rows = set()
    print_val_row()
    num = input('по какому значению ищем? (можно несколько через запятую): ')
    search_column = [int(i) for i in num.split(',') if i.isdigit()]

    val = input('что ищем: ')
    for row in li:
        for col in search_column:
            if val in row[col]:
                finded_rows.add(f'{ROW_SEPARATOR}'.join(row))
    pprint_list(finded_rows, easy_li=True)


