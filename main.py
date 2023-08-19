from commands import get_list, new
from utils import check_db

def run():
    check_db()
    flag = True
    while(flag):
        flag = input('''\tq - выход
        l - вывести список на экран 
        n - новая запись
        e - редактировать 
        f - поиск \n''').lower()
        
        if flag == 'q':
            break
        elif flag== 'n':
            new.run()
        elif flag== 'l':
            get_list.run()
        else:
            print('неверно введена команда')
        

if __name__ == '__main__':
    run()