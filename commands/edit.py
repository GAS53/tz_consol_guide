from utils import get_rows, set_new_row
from settings import APPROVAL_LIST, DB_FILE


def edit_func(old_row: str):
    '''перезапись обновленного файла'''
    new_row = set_new_row()
    with open(DB_FILE, 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(old_row, new_row)
    with open(DB_FILE, 'w') as f:
        f.write(new_data)


def run():
    '''определение номера редактируемой строки'''
    li = get_rows()
    exit_flag = True
    while exit_flag:
        exit_flag = input('выход-"q", введите номер редактируемой строки: ')
        if exit_flag == 'q':
            break
        elif exit_flag.isdigit():
            exit_flag = int(exit_flag)
            if exit_flag > len(li):
                print('неверно задана строка')
            else:
                edit_row = input(f'Редактируем {li[exit_flag]}? y/n ')
                if edit_row in APPROVAL_LIST:
                    edit_func(li[exit_flag])
        else:
            print('неверное значение')
