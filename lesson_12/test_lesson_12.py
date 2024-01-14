# перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
# перевірити чи є ключ "value"  і перевірити його значення - 2 теста
# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести



import requests
import pytest

response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")


def test_response():
    assert response.status_code == 200


def test_empty_icon_url():
    assert response.json()["icon_url"] == "https://assets.chucknorris.host/img/avatar/chuck-norris.png"


def test_is_image():
    assert response.json()["icon_url"][-4:] == ".png"


def test_value_present():
    assert response.json()["value"]


def test_value_exists():
    assert response.json()[len("value")] < 0
