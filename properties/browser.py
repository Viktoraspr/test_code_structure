"""
Here we create driver and add all parameters.
Keep in mind, all tests should be run on known screen size.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import TestData


class Driver:
    """
    Create browser driver
    """

    def __init__(self):
        self.browser = TestData.BROWSER

    def __str__(self):
        return f'Browser is {self.browser}'

    def get_driver(self) -> webdriver:
        """
        Class returns browser's driver
        :return: web driver or None
        """
        match self.browser.lower():
            case "chrome":
                chrome_options = Chrome_options()
                chrome_options.add_argument(f"--window-size={TestData.BROWSER_WINDOW_SIZE}")
                chrome_options.add_argument("enable-automation")
                if TestData.BROWSER_MODE == 'headless':
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--no-sandbox")  # running under root user in docker
                    chrome_options.add_argument("--disable-extensions")  # disables warning popup
                    chrome_options.add_argument("--disable-dev-shm-usage")  # avoids crashing docker
                return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        chrome_options=chrome_options)
            case "firefox":
                return webdriver.Firefox(executable_path=GeckoDriverManager().install())
            case 'edge':
                return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
            case _:
                raise Exception(f'Not supported browser: {self.browser}')
