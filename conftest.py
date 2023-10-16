import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireOptions
from selenium.webdriver.chrome.options import Options

opts_firefox = FireOptions()
opts_chrome = Options()


def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default='headless',
                     help='By default is headless but you can set --browser mode="gui"')
    parser.addoption('--browser_size', action='store', default='fullscreen',
                     help='By default is fullscreen but you can set --browser_size = "half"')
    parser.addoption('--browser_choose', action='store', default='chrome',
                     help='By default is chrome but you can set --browser_choose = "firefox"')


@pytest.fixture(scope='function')
def browser(request):
    print("\nstart browser for test..")
    options = opts_chrome
    fire_options = opts_firefox
    browser_mode = request.config.getoption("browser_mode")

    if browser_mode == 'gui':
        print(f"\nbrowser mode: {browser_mode}")
    elif browser_mode == 'headless':
        options.add_argument('--headless')
        fire_options.add_argument('--headless')
        print(f"\nbrowser mode: {browser_mode}")
    else:
        print("Неверный режим запуска")
    browser_size = request.config.getoption("browser_size")

    if browser_size == 'fullscreen' and browser_mode == 'gui':
        print(f'\n browser size mode: {browser_mode}')
        options.add_argument('--start_maximized')
        fire_options.add_argument('--start_maximized')
    elif browser_size == 'half' and browser_mode == 'gui':
        print(f'\n browser size mode: {browser_mode}')
        options.add_argument('--window-size=960x1080 ')
        fire_options.add_argument('--window-size=960x1080 ')

    browser_choose = request.config.getoption('browser_choose')

    if browser_choose == 'chrome':
        browser = webdriver.Chrome(options=options)
    elif browser_choose == 'firefox':
        browser = webdriver.Firefox(options=fire_options)
    else:
        print('Choose chrome or firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()
