import pytest
from selenium import webdriver
from selenium.webdriver.ie.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome, firefox, ie, yandex or edge")

    @pytest.fixture(scope="function")
    def browser(request):
        browser_name = request.config.getoption("browser_name")
        browser = None
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome()
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.download.folderList", 2)
            fp.set_preference("browser.download.manager.showWhenStarting", False)
            fp.set_preference("browser.download.dir", 'C:\\Users\AkhmetzyanovaGL\\Downloads\\')
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf ")
            fp.set_preference("pdfjs.disabled", True)
            browser = webdriver.Firefox(firefox_profile=fp)
        elif browser_name == "ie":
            print("\nstart ie browser for test..")
            ie_options = Options()
            ie_options.ignore_protected_mode_settings = True
            ie_options.ignore_zoom_level = True
            browser = webdriver.Ie(executable_path=r'C:\\IEdriver\\IEDriverServer.exe', options=ie_options)
        elif browser_name == "yandex":
            print("\nstart yandex browser for test..")
            yandex_options = webdriver.ChromeOptions()
            yandex_options.binary_location = 'C:\\Users\\AkhmetzyanovaGL\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe'
            browser = webdriver.Chrome(executable_path=r'C:\\chromedriver79\\chromedriver.exe',
                                       chrome_options=yandex_options)
        elif browser_name == 'edge':
            print("\nstart edge browser for test..")
            browser = webdriver.Edge(executable_path=r'C:\\edgedriver\\msedgedriver.exe')
        else:
            raise pytest.UsageError("--browser_name should be chrome, firefox, ie, yandex or edge")
        yield browser
        print("\nquit browser..")
        browser.quit()
