from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.driver.maximize_window()
        self.full_name_field = (By.ID, "userName")
        self.full_email_field = (By.ID, "userEmail")
        self.full_current_area_field = (By.CSS_SELECTOR, "textarea#currentAddress")
        self.full_permanent_area_field = (By.CSS_SELECTOR, "textarea#permanentAddress")
        self.submit_btn = (By.ID, "submit")

        self.result_fullname = (By.ID, "name")
        self.email_result = (By.ID, "email")
        self.current_address_result = (By.CSS_SELECTOR, "p#currentAddress")
        self.permanent_address_result = (By.CSS_SELECTOR, "p#permanentAddress")

    def clear_input(self, selector):
        self.driver.find_element(selector).clear()

    def open(self) -> "TextBoxPage":
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.clear_input(*self.full_name_field)

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)

    def click_submit(self) -> None:
        self.driver.find_element(*self.submit_btn).click()

    def clear_email_filed(self) -> None:
        self.clear_input(*self.full_email_field)

    def fill_email_filed(self, text: str) -> None:
        self.driver.find_element(*self.full_email_field).send_keys(text)

    def clear_current_area_field(self) -> None:
        self.clear_input(*self.full_current_area_field)

    def fill_current_area_field(self, text: str) -> None:
        self.driver.find_element(*self.full_current_area_field).send_keys(text)

    def clear_permanent_area_field(self) -> None:
        self.clear_input(*self.full_permanent_area_field)

    def fill_permanent_area_field(self, text: str) -> None:
        self.driver.find_element(*self.full_permanent_area_field).send_keys(text)

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")

    def get_result_fullname(self):
        return self.driver.find_element(*self.result_fullname).text

    def get_email_result(self):
        return self.driver.find_element(*self.email_result).text

    def get_current_address_result(self):
        return self.driver.find_element(*self.current_address_result).text

    def get_permanent_address_result(self):
        return self.driver.find_element(*self.permanent_address_result).text
