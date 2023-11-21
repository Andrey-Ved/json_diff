from json import dumps

from src.data import TelegramMessage, example_message
from src.fake_data import random_data_cut
from src.calculation import find_diff


def json_print(json_: TelegramMessage) -> None:
    print(
        dumps(
            json_,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    )


def demo() -> None:
    print('\n'
          '*********** first ***********')
    j_1 = random_data_cut(example_message)
    json_print(j_1)

    print('********** second ***********')
    j_2 = random_data_cut(example_message)
    json_print(j_2)

    print('*********** diff ***********')
    j_diff = find_diff(j_1, j_2)
    json_print(j_diff)


if __name__ == '__main__':
    demo()
