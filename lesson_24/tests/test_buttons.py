from lesson_24.ButtonsPage import ButtonsPage
from selenium.webdriver.support import expected_conditions as ec


class TestButtons:

    def test_username_fill_and_check(self, chrome):
        page = ButtonsPage(chrome)
        page.open()
        # page.scroll_down()
        page.click_single_click_button()
        result = page.get_single_click_result()
        assert result == "You have done a dynamic click"


