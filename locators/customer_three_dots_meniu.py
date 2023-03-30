"""
File contains customer tab three dot menu all fields and their locators.

I use all_fields method to define all possible fields of table, menu, etc. Then you can iterate them and to check.
"""
from selenium.webdriver.common.by import By

from locators.locator_forms import SimpleLocatorForm


class ThreeDotsMenu:
    """
    Three dots menu
    """

    def __init__(self):
        self.show_trips = SimpleLocatorForm(name='Show trips',
                                            locator=(By.XPATH, '//button[contains(text(),"Show Trips")]'))
        self.show_fleet = SimpleLocatorForm(name='Show fleet',
                                            locator=(By.XPATH, '//button[contains(text(),"Show Fleet")]'))
        self.show_transactions = SimpleLocatorForm(name='Show transactions',
                                                   locator=(By.XPATH, '//button[contains(text(),"Show Transactions")]'))
        self.export = SimpleLocatorForm(name='Export',
                                        locator=(By.XPATH, '//button[contains(text(),"Export")]'))
        self.edit = SimpleLocatorForm(name='Edit',
                                      locator=(By.XPATH, '//button[contains(text(),"Edit")]'))
        self.delete = SimpleLocatorForm(name='Delete',
                                        locator=(By.XPATH, '//button[contains(text(),"Delete")]'))
        self.delete_confirm = SimpleLocatorForm(name='Delete confirm',
                                                locator=(By.XPATH,
                                                         '//div[contains(@class, "confirm")]//button[@label="Delete"]'))

    def all_fields(self) -> list:
        """
        :return: All possible field in three dot menu
        """
        return [self.show_trips, self.show_fleet, self.show_transactions, self.export, self.edit, self.delete]
