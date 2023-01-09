from flask import Flask, request
from tinydb import TinyDB

from validators import get_type


app = Flask(__name__)
db = TinyDB('db.json')


@app.post("/get_form")
def get_form():
    form = dict(request.args)
    if match_template:= get_match_template(form):
        return match_template['name']
    return {k: get_type(v) for k, v in form.items()}

def get_match_template(form: dict):
    '''проходимся по всем шаблонам в базе данных, и возвращаем
    самое подходящее соответствие (максимальное число полей)'''
    match_tmps = [tmp for tmp in db.all() if is_match(tmp, form)]
    return max(match_tmps, key=len) if match_tmps else None

def is_match(template: dict, form: dict) -> bool:
    '''проверяет соответсвует ли шаблон из базы данных (template)
    полученной форме от пользователя (form).
    проверяется имя поля и соответсвие типу данных поля'''
    for field_name, value_type in template.items():
        if field_name == 'name': continue
        if field_name not in form.keys():
            return False 
        if not get_type(form[field_name]) == value_type:
            return False
    return True