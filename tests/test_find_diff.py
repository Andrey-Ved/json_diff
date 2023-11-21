from src.calculation import find_diff
from tests.test_data import message_1, message_2, result_message


def test_find_diff():
    assert find_diff(message_1, message_2) == result_message
