from example import add_numbers


def test_adding_two_numbers():
    number_1 = 5
    number_2 = 10
    assert add_numbers(number_1, number_2) == 15


def test_adding_multiple_numbers():
    number_1 = 1
    number_2 = 1
    number_3 = 1
    number_4 = 10
    assert add_numbers(number_1, number_2, number_3, number_4) == 13