from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ButtonsPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.maximize_window()
        self.url = "https://demoqa.com/buttons"
        self.single_click_button = (By.XPATH, "//button[.='Click Me']")
        self.single_click_message = (By.ID, "dynamicClickMessage")

    def open(self):
        self.driver.get(self.url)
        return self

    def click_single_click_button(self):
        self.driver.find_element(*self.single_click_button).click()

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")

    def get_single_click_result(self):
        self.driver.find_element(*self.single_click_message).text

