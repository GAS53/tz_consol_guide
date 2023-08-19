from settings import DB_FILE
from utils import set_new_row


def run():
    '''добавление новой строки'''
    row = set_new_row()
    with open(DB_FILE, 'a') as file:
        file.write(row)