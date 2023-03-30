"""
Navigation bar in the main logged page: structure, locators...


I use tabs_list method to define all possible fields of table, menu, etc. Then you can iterate them and to check.
"""
from selenium.webdriver.common.by import By

from locators.locator_forms import SimpleLocatorForm


class NavigationLocators:
    """
    Class for Navigation locators
    """

    def __init__(self):
        self.logo = SimpleLocatorForm(name='Logo',
                                      locator=(By.XPATH, '//a[contains(@class, "logo")]'))
        self.dashboard = SimpleLocatorForm(name='Dashboard',
                                           locator=(By.XPATH, '//div[contains(@class, "top-nav")]//a[@href="/"]'))
        self.map = SimpleLocatorForm(name='Map',
                                     locator=(By.XPATH, '//a[contains(@href, "trips")]'),
                                     url='trips')
        self.fleet = SimpleLocatorForm(name='Fleet',
                                       locator=(By.XPATH, '//a[contains(@href, "fleet")]'),
                                       url='fleet')
        self.transaction = SimpleLocatorForm(name='Transaction',
                                             locator=(By.XPATH, '//a[contains(@href, "transactions")]'),
                                             url='transactions', )
        self.statements = SimpleLocatorForm(name='Statements',
                                            locator=(By.XPATH, '//a[contains(@href, "statement")]'),
                                            url='statement-management')
        self.users = SimpleLocatorForm(name='Users',
                                       locator=(By.XPATH, '//a[contains(@href, "users")]'),
                                       url='users', )
        self.customers = SimpleLocatorForm(name='Customers',
                                           locator=(By.XPATH, '//nav//a[contains(@href, "custom")]'),
                                           url='customers')
        self.select_customer = SimpleLocatorForm(name='Select customer',
                                                 locator=(By.XPATH, '//div[contains(@class, "active-customer")]'))
        self.sing_out = SimpleLocatorForm(name='Sing out',
                                          locator=(By.XPATH, '//a[contains(@href, "login")]'),
                                          url='login')

    def tabs_list(self) -> list:
        """
        :return: all tabs in main page
        """
        return [self.logo, self.dashboard, self.map, self.fleet, self.transaction, self.statements, self.users,
                self.customers, self.select_customer, self.sing_out]
