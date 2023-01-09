import re
from datetime import datetime


def is_time(str_value):
    '''проверяет является ли строка - датой (DD.MM.YYYY|YYYY-MM-DD)'''
    try:
        if '.' in str_value:
            return datetime.strptime(str_value, '%d.%m.%Y')
        return datetime.fromisoformat(str_value)
    except ValueError:
        return False

check_funcs = {
    'date': is_time,
    'phone': lambda s: re.match(r'[\+ ]?7 \d{3} \d{3} \d\d \d\d', s),
    'email': lambda s: re.match(r'[\w\-\.]+@[a-z]+\.?[a-z]+\.[a-z]{2,4}', s),
}

def get_type(value: str) -> str:
    '''определяет тип данных и возвращает имя типа данных'''
    for type_name, func in check_funcs.items():
        if func(value):
            return type_name 
    return 'text'