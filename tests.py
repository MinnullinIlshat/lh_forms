import json

from app import app
from test_cases import test_cases


def test_form_get():
    test_count, failed = 0, 0
    print('< test session starts >'.center(60, '='))
    for post_query, expected_response in test_cases:
        query = '&'.join([f'{k}={v}' for k, v in post_query.items()]) # создаем строку запроса из словаря
        response = app.test_client().post(f'/get_form?{query}')
        if '{' in (res_data:= response.data.decode('utf-8')): # декодируем строку в res_data
            res_data = json.loads(res_data)                   # если строка в json, превращаем в словарь
        test_count += 1
        try:
            assert res_data == expected_response
            print(f"{test_count}: test passed!")
        except AssertionError:
            failed += 1
            print(f"{test_count}: test failed!")
    print(f'< {failed} tests failed! >'.center(60, '='))

test_form_get()