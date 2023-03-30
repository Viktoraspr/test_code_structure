from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from locators.customer_three_dots_meniu import ThreeDotsMenu
from locators.customers_table import Customer_Table_Menu, Customer_Table
from locators.locator_forms import SimpleLocatorForm, CallSimpleLocatorForm
from methods.helper_selenium_methods import HelperMethods
from data_for_tests.data_dataclass_forms import Customer


class WebPortalMainPage(HelperMethods, ThreeDotsMenu):
    # UI objects with selector
    save_button = SimpleLocatorForm(name='Save',
                                    locator=(By.XPATH, "//button[text()='Save']"))
    customers_header = SimpleLocatorForm(name='Customer header',
                                         locator=(By.XPATH, '//h3[text()="customers"]'))
    add_new_customer_button = SimpleLocatorForm(name='New customer button',
                                                locator=(By.XPATH, '//button[@label="Add new customer"]'))
    add_new_user_button = SimpleLocatorForm(name='New user button',
                                            locator=(By.XPATH, '//button[@label="Add new user"]'))
    company_name_field = SimpleLocatorForm(name='Company name field',
                                           locator=(By.XPATH, '//input[@name="companyName"]'))
    admin_email_field = SimpleLocatorForm(name='Admin name field',
                                          locator=(By.XPATH, '//input[@name="adminEmail"]'))
    company_address_field = SimpleLocatorForm(name='Company address field',
                                              locator=(By.XPATH, '//input[@name="address"]'))
    geotab_database_field = SimpleLocatorForm(name='Geotab database field',
                                              locator=(By.XPATH, '//input[@name="geotabDatabase"]'))
    geotab_service_user_field = SimpleLocatorForm(name='Geotab service user field',
                                                  locator=(By.XPATH, '//input[@name="geotabServiceUser"]'))
    geotab_service_password_field = SimpleLocatorForm(name='Geotab service user field',
                                                      locator=(By.XPATH, '//input[@name="geotabServicePassword"]'))
    name_field = SimpleLocatorForm(name="Name field",
                                   locator=(By.XPATH, '//input[@name="name"]'))
    first_name_field = (By.XPATH, "//input[@name='firstName']")
    last_name_field = (By.XPATH, "//input[@name='lastName']")
    user_email_field = (By.XPATH, "//input[@name='email']")
    attributed_role_field = (By.XPATH, "//label[@for='Attributed role*']/following-sibling::div")
    send_invite_button = SimpleLocatorForm(name='Send invite button',
                                           locator=(By.XPATH, "//button[@label='Send invite']"))
    yes_button = SimpleLocatorForm(name='Yes button',
                                   locator=(By.XPATH, '//button[text()="Yes"]'))
    close_button = SimpleLocatorForm(name='Close button',
                                     locator=(By.XPATH, "//button[text()='Close']"))
    continue_button = SimpleLocatorForm(name='Continue button',
                                        locator=(By.XPATH, "//button[text()='Continue']"))
    gear_icon = SimpleLocatorForm(name='Gear icon',
                                  locator=(By.XPATH, "//div[@class='row-action-icon_button-wrapper__b6Zdn']/button"))
    status_drag_button = (By.XPATH, "//h3[text()='status']/parent::section/following-sibling::span")
    company_name_drag_button = (By.XPATH, "//h3[text()='company name']/parent::section/following-sibling::span")
    search_button = (By.XPATH, "//button[@aria-label='searchbar-expand']")
    search_field = (By.XPATH, "//input[@id='search-input']")
    success_pop_up = SimpleLocatorForm(name='Success pop up',
                                       locator=(By.XPATH, "//section[contains(@class,'api-response_success')]"))
    success_pop_up_message = SimpleLocatorForm(
        name='Success pop up message',
        locator=(By.XPATH, "//section[contains(@class,'api-response_success')]/h3"))
    header_title = SimpleLocatorForm(name='Header title',
                                     locator=(By.XPATH, '//h3[contains(@class, "page-title")]'))
    filter_button = (By.XPATH, "//div[contains(@class,'filters')]//button")
    company_filter_field = (By.XPATH, "//label[@for='Company']/following-sibling::div")
    show_results_button = (By.XPATH, "//button[text()='Show results']")
    reset_button = (By.XPATH, "//button[text()='Reset']")
    column_header = (By.XPATH, "//h4[contains(@class, 'item_heading')]")
    table_container = SimpleLocatorForm(name='Table container',
                                        locator=(By.XPATH, "//div[contains(@class, 'table_container')]"))
    # For these locators we need to send value
    three_dots_element = CallSimpleLocatorForm(
        name='Tree dots button',
        locator=(By.XPATH, '//span[text()="{value}"]/ancestor::div[contains(@class, '
                           '"row-text-content_container")]/following-sibling::div//span'))
    table_field = CallSimpleLocatorForm(name='Table field in Customer table',
                              locator=(By.XPATH, '//span[@title="{value}"]'))

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log

    def add_new_customer(self, customer: Customer) -> None:
        """
        Add new customer to Portal
        :param customer: Customer's data
        :return: None
        """
        self.log.info("Create new customer")
        self.do_click(self.add_new_customer_button)
        self.do_send_keys(self.company_name_field, customer.name)
        self.do_send_keys(self.admin_email_field, customer.email)
        self.do_send_keys(self.company_address_field, customer.address)
        if customer.integration == "Yes":
            self.do_click(self.yes_button)
        self.do_send_keys(self.geotab_database_field, customer.database)
        self.do_send_keys(self.geotab_service_user_field, customer.user)
        self.do_send_keys(self.geotab_service_password_field, customer.password)
        self.do_click(self.send_invite_button)

    # Returns list of elements by header column in Customers tab
    def return_list_of_table_elements(self, header, filtered_by_search):
        # ToDo: to do smarter - it's not clear what this function do.
        if header == "status":
            locator = '//p[contains(@class,"status")]//span[@class]'
        elif filtered_by_search is True:
            locator = f'//p[contains(@class,"{header}")]//mark'
        else:
            locator = f'//p[contains(@class,"{header}")]//span[@class=""]'
        print(locator)
        list_of_elements = self.driver.find_elements(By.XPATH, locator)
        list_of_strings = []
        for i in list_of_elements:
            list_of_strings.append(i.text)
        print(list_of_strings)
        return list_of_strings

    def click_customer_menu_options(self, company_name: str, field_in_menu: SimpleLocatorForm) -> None:
        """
        Click on three dots menu list in the Customers tab by the company name and status
        :param company_name: company, which should be selected from menu
        :param field_in_menu: blablabla
        :return: None
        """
        self.do_click(self.three_dots_element(company_name))
        self.do_click(field_in_menu)

    def change_column_order(self, drag_column: Customer_Table_Menu, drop_column: Customer_Table_Menu):
        """
        Change column order
        :param drag_column: column, which should be moved
        :param drop_column: column, before which drag column drops
        :return: None
        """
        self.log.info("Changes columns order")
        self.do_click(self.gear_icon)
        self.drag_and_drop(drag_column, drop_column)
        self.log.info(f'{drag_column.name} was dropped on column {drop_column.name}')
        self.do_click(Customer_Table().done_button)

    def filter_by_search_customer_tab(self, search_text) -> None:
        """
        For text input in search field
        :param search_text:text, which should be entered in search field
        :return:
        """
        self.log.info(f'Search: "{search_text}" in customer tab')
        self.do_click(Customer_Table().search_button)
        self.do_send_keys(Customer_Table().search_button, search_text)

    def activate_table_columns_in_customer_tab(self, columns: list[Customer_Table_Menu], activate: bool = True) -> None:
        """
        Activates/deactivates columns
        :param columns: columns, which should be activated/deactivated
        :param activate: True: column has be activated
        :return: None
        """
        log_text = 'Activating columns' if activate else "Removes columns"
        self.log.info(f'{log_text}: {columns}')
        self.do_click(self.gear_icon)
        for column in columns:
            status = self.locate_element(column.status_locator).get_attribute("data-switch-is-on")
            status = True if status == 'true' else False
            if activate != status:
                self.do_click(SimpleLocatorForm(name=column.name,
                                                locator=column.status_locator))

        self.do_click(Customer_Table().done_button)

    # Retrieves list of Headers
    def retrieve_headers_list(self):
        headers_list = []
        locator, xpath = self.column_header
        try:
            parent_obj = self.wait_until_element_presented(self.table_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    headers_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return headers_list

    def delete_customer(self, company_name) -> None:
        """
        delete customer in portal
        :param company_name: company_name, which should be deleted. In must be one row when add value in search field
        :return: None
        """
        self.log.info(f"Deletes customer {company_name}")
        self.filter_by_search_customer_tab(f'any-word {company_name}')
        elements = self.locate_elements(Customer_Table().company_name.column.table_field_locator)
        if elements:
            self.do_click(SimpleLocatorForm(name=Customer_Table().company_name.column.name,
                                            locator=Customer_Table().company_name.column.check_row))
            self.do_click(Customer_Table().delete)
            self.do_click(Customer_Table().delete_confirm)
            self.wait_until_element_disappear(Customer_Table().delete_confirmation_form)
        else:
            self.log.warn('It was not find row, which needed company')
        self.do_click(Customer_Table().search_cancel)
