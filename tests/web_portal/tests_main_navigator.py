"""
Web portal tests - checking main portal navigation.
If we don't know what to check or maybe if we know some bug - I suggest to write 'Todo:',
 and write comment or jira ticket number.

As you see, in theses tests we use all helpers function, locators from other folders.
"""
import unittest

import pytest
from selenium.common.exceptions import WebDriverException

from locators.locator_forms import SimpleLocatorForm
from locators.navigation_bar import NavigationLocators
from methods.helper_selenium_methods import HelperMethods
from methods.timer import Timer
from pages.web_portal_home_page import WebPortalHomePage
from pages.web_portal_login_page import WebPortalLoginPage
from pages.web_portal_main_page import WebPortalMainPage
from properties.browser import Driver
from properties.config import TestData
from properties.logs import Logger


class WebPortal(unittest.TestCase):
    """
    Web portal tests
    """
    log = Logger().logger
    helper_methods = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().get_driver()
        WebPortalLoginPage(cls.driver, cls.log).open_portal_and_sign_in()
        cls.helper_methods = HelperMethods(cls.driver, log=cls.log)
        cls.webPortal_home_page = WebPortalHomePage(cls.driver, cls.log)
        cls.webPortal_main_page = WebPortalMainPage(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.log.info("Closing WebPortal")
        cls.driver.quit()

    @pytest.mark.regression
    def test_no_01(self) -> None:
        """
        Check if all navigation menu exists and check if it works - redirect in correct url
        :return: None
        """
        navigation_field = NavigationLocators()

        field: SimpleLocatorForm
        for field in navigation_field.tabs_list():
            # Todo: It's unclear what should be checked in these selections
            if field.name in ('Select customer', 'Logo'):
                continue

            self.helper_methods.do_click(field=field)

            if field.name == 'Dashboard':
                timer = Timer()
                while not timer.fired():
                    try:
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        self.driver.close()
                        break
                    except (IndexError, WebDriverException):
                        continue
                self.driver.switch_to.window(self.driver.window_handles[0])

            assert self.driver.current_url == f'{TestData.WEB_PORTAL_TOLL_LOGIC_URL}{field.url}'

            if field.name == 'Sing out':
                break

            for checking_locator in navigation_field.tabs_list():
                assert self.helper_methods.is_displayed(checking_locator)
