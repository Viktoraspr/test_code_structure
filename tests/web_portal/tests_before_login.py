"""
Web portal tests before login.
"""
import unittest

import pytest

from methods.helper_selenium_methods import HelperMethods
from pages.web_portal_home_page import WebPortalHomePage
from pages.web_portal_login_page import WebPortalLoginPage
from pages.web_portal_main_page import WebPortalMainPage
from properties.browser import Driver
from properties.config import TestData
from data_for_tests.data_for_tests import MESSAGE_CORRECT, MESSAGE_INCORRECT
from properties.logs import Logger


class TestsWithoutLogin(unittest.TestCase):
    """
    Web portal tests
    """
    log = Logger().logger
    helper_methods = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().get_driver()
        cls.helper_methods = HelperMethods(cls.driver, log=cls.log)
        cls.webPortal_home_page = WebPortalHomePage(cls.driver, cls.log)
        cls.webPortal_login_page = WebPortalLoginPage(cls.driver, cls.log)
        cls.webPortal_main_page = WebPortalMainPage(cls.driver, cls.log)
        cls.helper_methods.open_page(TestData.WEB_PORTAL_URL)

    @classmethod
    def tearDownClass(cls):
        cls.log.info("Closing WebPortal")
        cls.driver.quit()

    @pytest.mark.regression
    def test_no_01_first_page(self) -> None:
        """
        Commerce logic Home, Contact Us, Sign In button is visible.
        :return:  None
        """
        assert self.helper_methods.is_displayed(self.webPortal_home_page.slogan)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.login_button)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.contact_us_button_first)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.contact_us_button_second)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.commerce_logic)

    @pytest.mark.regression
    def test_no_02_contact_us(self) -> None:
        """
        Contact Us, Visit Us, Get in Touch information is visible
        :return: None
        """
        self.helper_methods.do_click(self.webPortal_home_page.contact_us_button_second)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.contact_us_container)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.visit_us_container)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.get_in_touch_container)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.map_container)

    @pytest.mark.regression
    def test_no_03_send_message_negative(self) -> None:
        """
        Fills name, organization, email, +37061234567, message, click Send message
        :return: None
        """
        self.webPortal_home_page.send_message(data=MESSAGE_INCORRECT)
        assert self.helper_methods.is_displayed(field=self.webPortal_home_page.container_error,
                                                timeout=3) or self.helper_methods.is_displayed(
            field=self.webPortal_home_page.message_error, timeout=3)

    @pytest.mark.regression
    def test_no_04_send_message_positive(self) -> None:
        """
        Fills name, organization, email, +37061234567, message, click Send message
        :return: None
        """
        self.webPortal_home_page.send_message(data=MESSAGE_CORRECT)
        assert self.helper_methods.is_displayed(self.webPortal_home_page.successful_message)
