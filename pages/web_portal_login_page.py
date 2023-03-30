"""This file using for portal login"""

from selenium.webdriver.common.by import By

from locators.locator_forms import SimpleLocatorForm
# pylint: disable=C0411 wrong-import-position
from methods.helper_selenium_methods import HelperMethods
from properties.config import TestData
from users.users import WB_USER
from users.users_forms import WebUser


class WebPortalLoginPage(HelperMethods):
    """
    Class for login in portal
    """
    email_field = SimpleLocatorForm(name='"Email" in Login Page',
                                    locator=(By.XPATH, '//input[@type="email"]'))
    password_field = SimpleLocatorForm(name='Password in Login field',
                                       locator=(By.XPATH, "//input[@type='password']"))
    sign_in_button = SimpleLocatorForm(name='"Sing in" in Login page',
                                       locator=(By.XPATH, '//button[text()="Sign in"]'))

    def sign_in(self, user: WebUser = WB_USER) -> None:
        """
        SingIn to portal
        :param user: WebUser, who contains name, passwords, etc...
        :return: None
        """
        self.do_send_keys(self.email_field, user.email)
        self.do_send_keys(self.password_field, user.password)
        self.do_click(self.sign_in_button)

    def open_portal_and_sign_in(self, user: WebUser = WB_USER, url=TestData.WEB_PORTAL_TOLL_LOGIC_URL) -> None:
        """
        SingIn to portal
        :param user: WebUser, who contains name, passwords, etc...
        :return: None
        """
        self.log.info("Opening WebPortal")
        self.open_page(url=url)
        self.sign_in(user=user)
