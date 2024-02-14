import pytest
from selenium import webdriver


# @pytest.fixture(scope="class")
# def firefox(request):
#     driver = webdriver.Firefox(executable_path="/home/dima/PycharmProjects/Lessons/hillel_school/lesson_20/tests/chromedriver")
#     request.cls.driver = driver
#     driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
#     yield driver
#     driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="/home/dima/PycharmProjects/Lessons/hillel_school/lesson_20/tests/chromedriver")
    request.cls.driver = driver
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
