from utils.func import read_json, create_ex
from main import FILENAME
from utils.classes import Operation
from tests.testfixture import data_fixture


#FILENAME = os.path.join('../operations.json')

def test_read_json():
    assert type(read_json(FILENAME)) == list


def test_create_ex():
    assert type(create_ex(FILENAME)) == list


def test_get_date(data_fixture):
    operation = Operation(
                   data_fixture.get('id'),
                   data_fixture.get('date'),
                   data_fixture.get('state'),
                   data_fixture.get('operationAmount').get('amount'),
                   data_fixture.get('operationAmount').get('currency').get('code'),
                   data_fixture.get('description'),
                   data_fixture.get('to'),
                   data_fixture.get('from'),
                )
    assert operation.state == 'EXECUTED'
    operation.get_date()
    assert operation.date == '26.08.2019'
    operation.encode_from()
    assert operation.to == 'Счет 64686473678894779589'
