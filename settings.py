from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent  # базовая директория
DB_PATH = BASE_PATH / 'database'  # директория с файлом с данными
DB_FILE = DB_PATH / 'db.txt'  # путь к файлу с данными
ROW_PARAMS = ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный (сотовый)']  # параметры для одной строки
ROW_SEPARATOR = '*'  #  разделитель данных в строке
PER_PAGE = 3  # количество выводимых на странице данных при запроесе списка
APPROVAL_LIST = ['y', 'yes', 'да', 'д']  # согласие
