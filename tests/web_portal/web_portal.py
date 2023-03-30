"""
Web portal tests - checking functionality of portal.
If we don't know what to check or maybe if we know some bug - I suggest to write 'Todo:',
 and write comment or jira ticket number.

As you see, in theses tests we use all helpers function, locators from other folders.

Also it's possible use parameterized: https://pypi.org/project/parameterized/
"""
import unittest

import HtmlTestRunner
import pytest
from parameterized import parameterized

from locators.customer_three_dots_meniu import ThreeDotsMenu
from locators.customers_table import Customer_Table
from locators.locator_forms import SimpleLocatorForm
from locators.navigation_bar import NavigationLocators
from methods.helper_selenium_methods import HelperMethods
from pages.web_portal_home_page import WebPortalHomePage
from pages.web_portal_login_page import WebPortalLoginPage
from pages.web_portal_main_page import WebPortalMainPage
from properties.browser import Driver
from properties.config import TestData
from data_for_tests.data_for_tests import CUSTOMER_DEFAULT, CUSTOMER_NEW, CUSTOMER_EDITED
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
        cls.helper_methods = HelperMethods(cls.driver, log=cls.log)
        cls.webPortal_home_page = WebPortalHomePage(cls.driver, cls.log)
        cls.webPortal_login_page = WebPortalLoginPage(cls.driver, cls.log)
        cls.webPortal_main_page = WebPortalMainPage(cls.driver, cls.log)

    @classmethod
    def tearDownClass(cls):
        cls.log.info("Closing WebPortal")
        cls.driver.quit()

    @pytest.mark.regression
    def test_no_01(self) -> None:
        """
        Enters e-mail, password e.g. Folajire@1108, clicks Sign in
        :return: None
        """
        self.webPortal_login_page.open_portal_and_sign_in()
        assert self.helper_methods.is_displayed(self.webPortal_main_page.customers_header)

    @pytest.mark.regression
    def test_no_02(self) -> None:
        """
        adds new customer: Company name, email, address, geotab, geotab integretion, etc..
        Clicks invite
        :return: None
        """
        self.webPortal_main_page.add_new_customer(CUSTOMER_NEW)
        checking_fields = all([
            self.helper_methods.is_displayed(self.webPortal_main_page.success_pop_up),
            self.helper_methods.is_displayed(self.webPortal_main_page.success_pop_up_message),
            self.helper_methods.get_text_from_element(
                self.webPortal_main_page.success_pop_up_message) == "Customer added successfully",
        ])

        if not checking_fields:
            self.webPortal_main_page.do_click(self.webPortal_main_page.close_button)

        self.helper_methods.do_click(self.webPortal_main_page.continue_button)
        assert checking_fields

    @pytest.mark.regression
    def test_no_03(self) -> None:
        """
        Click three dots on the customer Test, click Edit, change company name and address, click done
        :return: None
        """
        self.webPortal_main_page.click_customer_menu_options(company_name=CUSTOMER_NEW.name,
                                                             field_in_menu=ThreeDotsMenu().edit)
        self.helper_methods.do_send_keys(self.webPortal_main_page.company_name_field, CUSTOMER_EDITED.name)
        self.helper_methods.do_send_keys(self.webPortal_main_page.company_address_field, CUSTOMER_EDITED.address)
        self.helper_methods.do_click(self.webPortal_main_page.save_button)
        locator = self.webPortal_main_page.table_field(CUSTOMER_EDITED.name)
        # Todo: it's possible, it will not work when we have a lot of customers.
        #  Need to do filter and just then delete
        #  Need to delete customer using an API request
        assert self.helper_methods.is_displayed(locator)

    @pytest.mark.regression
    def test_no_04(self) -> None:
        """
        Click three dots on the welink customer, click Show Trips"
        :return: None
        """
        self.webPortal_main_page.click_customer_menu_options(company_name=CUSTOMER_DEFAULT.name,
                                                             field_in_menu=ThreeDotsMenu().show_trips)
        checking_fields = all([
            self.helper_methods.get_text_from_element(self.webPortal_main_page.header_title) == "Trips",
            self.helper_methods.is_displayed(self.webPortal_main_page.table_container),
        ])
        self.helper_methods.do_click(NavigationLocators().customers)
        assert checking_fields

    @pytest.mark.regression
    def test_no_05(self) -> None:
        """
        Click three dots on the welink customer, click Show Fleet
        :return: None
        """
        self.webPortal_main_page.click_customer_menu_options(company_name=CUSTOMER_DEFAULT.name,
                                                             field_in_menu=ThreeDotsMenu().show_fleet)
        checking_fields = all(
            [self.helper_methods.get_text_from_element(self.webPortal_main_page.header_title) == "Fleet",
             self.helper_methods.is_displayed(self.webPortal_main_page.table_container)])
        self.helper_methods.do_click(NavigationLocators().customers)
        assert checking_fields

    @pytest.mark.regression
    def test_no_06(self) -> None:
        """
        Click three dots on the welink customer, click 'Show Transactions'
        :return:  None
        """
        self.webPortal_main_page.click_customer_menu_options(company_name=CUSTOMER_DEFAULT.name,
                                                             field_in_menu=ThreeDotsMenu().show_transactions)
        checking_fields = all(
            [self.helper_methods.get_text_from_element(self.webPortal_main_page.header_title) == 'Transactions',
             self.helper_methods.is_displayed(self.webPortal_main_page.table_container)])
        self.webPortal_main_page.do_click(NavigationLocators().customers)
        assert checking_fields

    @pytest.mark.regression
    def test_no_07(self) -> None:
        """
        Clicks gear button, unchecks admin email, check if disappear column from table
        and then again activate column.
        :return: None
        """
        self.webPortal_main_page.do_click(NavigationLocators().customers)
        column = Customer_Table().admin_mail
        columns = [column.menu]
        self.webPortal_main_page.activate_table_columns_in_customer_tab(columns=columns, activate=False)
        checking_result = [self.helper_methods.wait_until_element_disappear(
            field=SimpleLocatorForm(name=column.column.name,
                                    locator=column.column.locator))]
        self.webPortal_main_page.activate_table_columns_in_customer_tab(columns=columns, activate=True)
        checking_result.append(self.helper_methods.is_displayed(column.column))
        assert all(checking_result)

    @pytest.mark.regression
    def test_no_08(self) -> None:
        """
        Change column order
        :return: None
        """
        customer_table = Customer_Table()
        drag_column = customer_table.status.menu
        drop_column = customer_table.company_name.menu
        columns_before_changes = self.helper_methods.get_text_from_elements(customer_table.table_column_header)
        drag_column_index = columns_before_changes.index(drop_column.name.upper())
        columns_before_changes.remove(drag_column.name.upper())
        columns_before_changes.insert(drag_column_index, drag_column.name.upper())
        self.webPortal_main_page.change_column_order(drag_column, drop_column)
        columns_after_changes = self.helper_methods.get_text_from_elements(customer_table.table_column_header)
        self.helper_methods.do_click(self.webPortal_main_page.gear_icon)
        self.helper_methods.do_click(customer_table.set_to_default_button)
        try:
            assert columns_after_changes == columns_before_changes
        except AssertionError:
            raise AssertionError(
                f'Columns before changes: {columns_after_changes}, columns after changes: {columns_before_changes}')

    @pytest.mark.regression
    @parameterized.expand([
        (CUSTOMER_DEFAULT.name,),
        ('@test',),
        ('active',),
        ('florida',),
    ])
    def test_no_09(self, filtering_value: str) -> None:
        """
        Add value in search field and check if searching works.
        :param: filtering_value: values, which should be checked.
        :return: None
        """
        # Todo: Selenium can't send first word in Search field, probably bug in portal
        self.webPortal_main_page.filter_by_search_customer_tab(f'any-word {filtering_value}')
        table_data = {}
        for index, column in enumerate(Customer_Table().all_columns()):
            table_data[index] = self.helper_methods.get_text_from_elements(
                field=SimpleLocatorForm(name=column.name,
                                        locator=column.table_field_locator))
        self.helper_methods.do_click(Customer_Table().search_cancel)
        # Todo: bug in portal:
        rows_number = len(table_data)
        for i in range(len(table_data[0])):
            rows_value = []
            for columns in range(rows_number):
                rows_value.append(table_data[columns][i])
            assert filtering_value in ' '.join(rows_value).lower()


    @pytest.mark.regression
    def test_no_12(self) -> None:
        """
        Test works only then, when get value in filtered rows
        :return: None
        """
        self.webPortal_main_page.delete_customer(CUSTOMER_EDITED.name)
        self.helper_methods.wait_until_element_disappear(
            SimpleLocatorForm(name=Customer_Table().company_name.column.name,
                              locator=Customer_Table().company_name.column.table_field_locator))

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=TestData.reports_path))
