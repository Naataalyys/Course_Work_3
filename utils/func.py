import json
from utils.classes import Operation
import os


def read_json(file_name):
    """Читает json файл"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def create_ex():
    """Создаёт экземпляр класса"""
    json_file = read_json(os.path.join('utils', 'operations.json'))

    ex_class = []
    for num, oper in enumerate(json_file):

        try:
            ex_class.append(
                Operation(
                    oper.get('id'),
                    oper.get('date'),
                    oper.get('state'),
                    oper.get('operationAmount').get('amount'),
                    oper.get('operationAmount').get('currency').get('code'),
                    oper.get('description'),
                    oper.get('to'),
                    oper.get('from'),
                )
            )
        except TypeError:
            print(f'Невалидные данные в операции № {num}')
            continue
        except AttributeError:
            print(f'Невалидные данные в операции № {num}')
            continue

    ex_class.sort(key=lambda d: (d.state, d.date), reverse=True)
    return ex_class
