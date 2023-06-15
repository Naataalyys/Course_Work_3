from utils.func import create_ex
from pathlib import Path

CURRENT_PATH = Path(__file__).parent
FILENAME = Path.joinpath(CURRENT_PATH, 'operations.json')


def main():
    list_ex = create_ex(FILENAME)

    for ex in list_ex[:5]:
        ex.get_date()
        ex.encode_to()
        ex.encode_from()
        print(ex.beautiful_output())


if __name__ == '__main__':
    main()
