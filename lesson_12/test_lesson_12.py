# # перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
# # перевірити чи є ключ "value"  і перевірити його значення - 2 теста
# # Зробити окремий клас
# # пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# # зробити класому фікстуру
# # тест на статус код
# # тест на кількість жартів
# # тест на сам жарт
# # + 3 тести

import pytest


@pytest.mark.usefixtures("fixture_random")
class TestRandom:

    def test_response(self, fixture_random):
        assert self.status_code == 200

    def test_empty_icon_url(self, fixture_random):
        assert self.response.json()["icon_url"] == "https://assets.chucknorris.host/img/avatar/chuck-norris.png"

    def test_is_image(self, fixture_random):
        assert self.response.json()["icon_url"][-4:] == ".png"

    def test_value_present(self, fixture_random):
        assert self.response.json()["value"]

    def test_value_exists(self, fixture_random):
        assert len(self.response.json()["value"]) > 0


@pytest.mark.usefixtures("fixture_query")
class TestQuery:

    def test_response(self, fixture_query):
        assert self.status_code == 200

    def test_jokes_amount(self, *fixture_query):
        assert self.response.json()["total"] == 23

    def test_joke_exist(self, fixture_query):
        result = self.response.json()["result"]
        value = len(result[0].get("value"))
        assert value > 0

    def test_first_joke_created_at(self, fixture_query):
        result = self.response.json()["result"]
        created_at = result[0].get("created_at").split()
        assert created_at[0] == '2020-01-05'

    def test_is_first_id_empty(self, fixture_query):
        result = self.response.json()["result"]
        id = len(result[0].get("id"))
        assert id > 0

    def test_text_last_joke(self, fixture_query):
        result = self.response.json()["result"]
        value = result[-1].get("value")
        assert value == "Chuck Norris loves to dance in the rain - acid rain."

