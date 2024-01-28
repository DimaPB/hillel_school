import time
from lesson_17.TextBoxPage import TextBoxPage


class TestTextBox:
    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        time.sleep(2)
        page.fill_full_name_field("Dimon")
        time.sleep(3)

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_filed("@email.com")
        time.sleep(3)

    def test_current_area_field(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_area_field("Baker Street 221b")
        time.sleep(3)
