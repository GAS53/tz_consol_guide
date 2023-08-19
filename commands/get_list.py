import math

from utils import get_rows, pprint_list
from settings import PER_PAGE


def run():
    '''вывод данных с разбивкой по страницам'''
    li = get_rows()
    max_len = len(li)
    all_pages = math.ceil(max_len / PER_PAGE)
    
    print(f'всего страниц {all_pages}')
    quit_flag = True
    while quit_flag:
        quit_flag = input('''q - выход, введите номер страници: ''')
        if quit_flag == 'q':
            break
        elif quit_flag.isdigit() and int(quit_flag) != 0:

            find_num = int(quit_flag)
            if find_num > all_pages:
                print('заданное число больше чем количество страниц')
            else:
                zero_index = (find_num - 1) * PER_PAGE
                result_li = [(i + zero_index, li[i + zero_index]) if i + zero_index < max_len else None for i in range(PER_PAGE)]
                pprint_list(result_li, easy_li=False)
        else:
            print('неверная команда нужен "q" или номер страници')
