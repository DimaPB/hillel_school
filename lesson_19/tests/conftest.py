import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/home/user/PycharmProjects/Lessons/hillel_school/lesson_19/chromedriver")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()



