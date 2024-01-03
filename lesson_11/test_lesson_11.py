# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
#  Запустіть цей ваш унікальний тест з маркером -k
#  додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли)
#  і біля скріншотів пропишіть команди які ви використовували.
#

import time
import pytest


def test_1():
    assert True
    time.sleep(2)


def test_2():
    assert True
    time.sleep(2)


def test_3():
    assert True
    time.sleep(2)


def test_4():
    assert True
    time.sleep(2)


def test_5():
    assert True
    time.sleep(2)
