from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
DB_PATH = BASE_PATH / 'database'
DB_FILE = DB_PATH / 'db.txt'
ROW_PARAMS = ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный (сотовый)']
ROW_SEPARATOR = '*'
PER_PAGE = 3
APPROVAL_LIST = ['y', 'yes', 'да', 'д']
