import pytest
import datetime
import time
from lesson_15 import Calculator


class TestCalculator:

    @classmethod
    def setup_class(cls):
        current_datetime = datetime.datetime.now()
        message = "Test started at {}".format(current_datetime)
        with open("test_logs.txt", 'a') as file:
            file.write("{}\n".format(message))

    @pytest.mark.parametrize("a, b, result", [(1, 3, 4), (1, 2, 3),
                                              (2, 3, 5), (2, 4, 6), (4, 5, 9)])
    def test_adding(self, a, b, result):
        testo = Calculator()
        assert testo.adding(a, b) == result
        time.sleep(1)

    @pytest.mark.parametrize("a, b, result", [(6, 3, 2), (9, 3, 3),
                                              (16, 4, 4), (44, 4, 11), (1, 2, 0.5)])
    def test_division(self, a, b, result):
        testo = Calculator()
        assert testo.division(a, b) == result
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        current_datetime = datetime.datetime.now()
        message = "Test finished at {}".format(current_datetime)
        with open("test_logs.txt", 'a') as file:
            file.write("{}\n".format(message))
