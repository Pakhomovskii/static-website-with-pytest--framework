import os
import warnings
from pathlib import Path

import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['WDM_LOG_LEVEL'] = '1'


def config():
    path = Path(__file__).parent / "../config.yaml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()


headless_option_arguments = [
            '--headless',
            '--no-sandbox',
            '--disable-gpu',
            '--window-size=1920,1080',
]



class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        warnings.simplefilter("ignore", ResourceWarning)
        if config()['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            if config()['headless']:
                for option in headless_option_arguments:
                    options.add_argument(option)
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        elif config()['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config()['headless']:
                for option in headless_option_arguments:
                    options.add_argument(option)
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
