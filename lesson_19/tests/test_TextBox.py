from lesson_19.TextBoxPage import TextBoxPage


class TestTextBox:
    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Dima")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Dima"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_filed("totosha@email.com")
        page.scroll_down()
        page.click_submit()
        email_filed = page.get_email_result()
        assert email_filed.split(":")[1] == "totosha@email.com"

    def test_current_area_field(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_area_field("Baker Street 221b")
        page.scroll_down()
        page.click_submit()
        current_address = page.get_current_address_result()
        assert current_address.split(":")[1] == "Baker Street 221b"

    def test_permanent_area_fild(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_area_field("Baker Street 221c")
        page.scroll_down()
        page.click_submit()
        permanent_address = page.get_permanent_address_result()
        assert permanent_address.split(":")[1] == "Baker Street 221c"
