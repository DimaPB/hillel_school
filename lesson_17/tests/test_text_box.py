import time
import pytest
from lesson_17.TextBoxPage import TextBoxPage


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Dimon")
        time.sleep(5)
        page.scroll_down()
        time.sleep(5)
        page.click_submit()
        time.sleep(5)
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Dimon"

    @pytest.mark.parametrize("email", ["i@meta", "wrong email"])
    def test_email_fill_and_check_negative(self, chrome, email):
        page = TextBoxPage(chrome)
        page.open()
        time.sleep(5)
        page.fill_email_field(email)
        time.sleep(5)
        page.scroll_down()
        time.sleep(5)
        page.click_submit()
        time.sleep(5)
        class_of_field = page.get_email_field_element().get_attribute("class")
        assert "error" in class_of_field