import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/home/dima/PycharmProjects/Lessons/hillel_school/lesson_24/tests/chromedriver")
    yield driver
    driver.quit()
