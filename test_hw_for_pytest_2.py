import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    print('\nstart')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit')
    browser.quit()


@pytest.fixture(autouse=True)
def information():
    print('Начало теста')


@pytest.fixture(scope='class')
def test_suite_start():
    print('Начало работы test suite')


class TestSuite:

    def test_1(self, browser, test_suite_start):
        browser.get('https://casenik.com.ua/')
        browser.find_element(By.XPATH, '//input[@class="header_search_input tt-input"]')

    def test_2(self, test_suite_start):
        assert 4*3 == 12


class TestSuite2:
    def setup_method(self):
        print('start browser')
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print('quit browser')
        self.driver.quit()

    def test_2_1(self):
        self.driver.get('https://casenik.com.ua/')
        self.driver.find_element(By.XPATH, '//div[@class="logo logo-desk"]/a')
