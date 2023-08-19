from settings import DB_FILE, ROW_PARAMS, ROW_SEPARATOR


def set_new_row():
    result_row = ''
    for val_name in ROW_PARAMS:
        if result_row != '':
            result_row += ROW_SEPARATOR
        val = input(f'введите - {val_name}: ')
        result_row += val
    return result_row


def run():
    row = set_new_row()
    with open(DB_FILE, 'a') as file:
        file.write(row)