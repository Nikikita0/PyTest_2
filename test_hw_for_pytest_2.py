import pytest
from selenium.webdriver.common.by import By


class TestSuite:

    @pytest.mark.browser
    @pytest.mark.input
    def test_1(self, browser):
        browser.get('https://casenik.com.ua/')
        browser.find_element(By.XPATH, '//input[@class="header_search_input tt-input"]')

    @pytest.mark.math
    def test_2(self):
        assert 4*3 == 12

    @pytest.mark.browser
    @pytest.mark.href
    def test_3(self, browser):
        browser.get('https://casenik.com.ua/')
        browser.find_element(By.XPATH, '//div[@class="logo logo-desk"]/a')

    @pytest.mark.math
    @pytest.mark.wrong
    def test_4(self):
        assert 4+3 == 12

    @pytest.mark.math
    def test_5(self):
        assert 5*6 == 30
