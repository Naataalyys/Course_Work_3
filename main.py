from utils.func import create_ex


def main():
    list_ex = create_ex()

    for ex in list_ex[:5]:
        ex.get_date()
        ex.encode_to()
        ex.encode_from()
        print(ex.beautiful_output())


if __name__ == '__main__':
    main()
