import pytest
from lesson_9 import add_tree_numbers


# solution 1

def test_1():
    assert add_tree_numbers(1, 2, 3) == 6


def test_2():
    assert add_tree_numbers(-1, -2, -3) == -6


def test_3():
    assert add_tree_numbers(1.8, 2.2, 3) == 7


# solution 2

@pytest.mark.parametrize("number_1, number_2, number_3, result", [
    pytest.param(1, 2, 3, 6),
    pytest.param(-1, -2, -3, -6),
    pytest.param(1.2, 2.8, 3, 7.0)])
def test_set_1(number_1, number_2, number_3, result):
    assert add_tree_numbers(number_1, number_2, number_3) == result


# solution 3

test_list = [(1, 2, 3, 6), (-1, -2, -3, -6), (1.8, 2.2, 3, 7)]


@pytest.mark.parametrize("number_1, number_2, number_3, result", test_list)
def test_3(number_1, number_2, number_3, result):
    assert add_tree_numbers(number_1, number_2, number_3) == result


