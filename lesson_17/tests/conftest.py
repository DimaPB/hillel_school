import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/home/user/PycharmProjects/Lessons/hillel_school/lesson_17/tests/chromedriver")
    yield driver
    driver.quit()
