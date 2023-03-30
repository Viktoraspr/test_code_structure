"""
Locators in customer page


I use all_fields method to define all possible fields of table, menu, etc. Then you can iterate them and to check.
"""

from selenium.webdriver.common.by import By

from locators.locator_forms import SimpleLocatorForm


class Customer_Table_Column:
    def __init__(self, name: str):
        self.name = name
        self.locator = (By.XPATH, f'//h4[text()="{name.lower()}"]')
        self.arrow_locator = (By.XPATH, f'//h4[text()="{name.lower()}"]/..//span')
        self.table_field_locator = (By.XPATH, f'//p[contains(@class, "customers-{name.lower().replace(" ", "-")}")]')
        self.check_row = (By.XPATH,
                          f'//p[contains(@class, "customers-{name.lower().replace(" ", "-")}")]'
                          f'/ancestor::section[contains(@class, "row")]//span[contains(@class, "check")]')


    def __str__(self):
        return f'{self.name}'


class Customer_Table_Menu:
    def __init__(self, name: str):
        self.name = name
        self.field_name_locator = (By.XPATH, f'//h3[text()="{name.lower()}"]')
        self.status_locator = (By.XPATH, f'//h3[text()="{name.lower()}"]/../button')
        self.six_dots_locator = (By.XPATH, f'//h3[text()="{name.lower()}"]/../..//span[@role="button"]')

    def __str__(self):
        return f'Table column class: {self.name}'


class Customer_Table_Field:
    def __init__(self, name):
        self.column = Customer_Table_Column(name=name)
        self.menu = Customer_Table_Menu(name=name)

    def __str__(self):
        return f'{self.column.name}'


class Customer_Table:
    def __init__(self):
        self.company_name = Customer_Table_Field(name='Company name')
        self.admin_mail = Customer_Table_Field(name='Admin E-mail address')
        self.address = Customer_Table_Field(name='Address')
        self.status = Customer_Table_Field(name='Status')
        self.done_button = SimpleLocatorForm(name='Done',
                                             locator=(By.XPATH, '//button[text()="Done"]'))
        self.cancel_button = SimpleLocatorForm(name='Cancel',
                                               locator=(By.XPATH, '//button[text()="Cancel"]'))
        self.set_to_default_button = SimpleLocatorForm(name='Set to default',
                                                       locator=(By.XPATH, '//button[text()="Set to default"]'))
        self.table_column_header = SimpleLocatorForm(name="Column header",
                                                     locator=(By.XPATH, "//h4[contains(@class, 'item_heading')]"))
        self.search_button = SimpleLocatorForm(name='Search',
                                               locator=(By.XPATH, '//button[@aria-label="searchbar-expand"]'))
        self.search_cancel = SimpleLocatorForm(name='Cancel search',
                                               locator=(By.XPATH, '//button[@aria-label="searchbar-cancel"]'))
        self.delete_confirmation_form = SimpleLocatorForm(name='Delete confirmation form',
                                                          locator=(By.XPATH, '//div[contains(@class, "confirm")]'))
        self.delete = SimpleLocatorForm(name='Delete',
                                        locator=(By.XPATH, '//button[@label="Delete"]'))
        self.delete_confirm = SimpleLocatorForm(name='Delete confirm',
                                                locator=(By.XPATH,
                                                         '//div[contains(@class, "confirm")]//button[@label="Delete"]'))

    def __str__(self):
        return f'Customer table. Columns: {self.admin_mail}, {self.status}, ' \
               f'{self.address}, {self.company_name} and the buttons.'

    def all_columns(self) -> list:
        """
        :return: all columns in list
        """
        return [self.company_name.column, self.admin_mail.column, self.address.column, self.status.column]
