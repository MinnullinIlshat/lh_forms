from tinydb import TinyDB
db = TinyDB('db.json')


templates = [
    {
        "name": "user_registration",
        "username": "text",
        "first_name": "text",
        "last_name": "text",
        "password": "text",
    },
    {
        "name": "newsletter",
        "email": "email",
    },
    {
        "name": "lead generation form",
        "phone_number": "phone",
        "email": "email",
    },
    {
        "name": "article",
        "title": "text",
        "body": "text",
        "username": "text",
        "current_date": "date",
    },
]

for template in templates:
    db.insert(template)