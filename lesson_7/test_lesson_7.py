from lesson_7 import sorted_list
from lesson_7 import reversed_list
from lesson_7 import words_list


def test_sorted_list():
    assert sorted_list([2, 1, 4, -1, 5, 1, 3]) == [-1, 1, 1, 2, 3, 4, 5]


def test_reversed_list():
    assert reversed_list([2, 1, 4, 5, 3]) == [5, 4, 3, 2, 1]


def test_sorted_words():
    assert (words_list(["apple", "juice", "rice", "tofu", "chips", "cola", "ice"]) ==
            ['ice', 'rice', 'tofu', 'cola', 'apple', 'juice', 'chips'])
