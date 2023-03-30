"""
File contains Selenium functions.

I suggest to create class, which would be used for Selenium function. Then not all team members must very deep
understand selenium functions, you just use such methods as find_element, click element, etc.

Before you write such methods, I suggest very carefully to read selenium documentation, to understand what is
implicit and explicit wait (in big project - explicit wait, for smaller - it can be implicit). Very important to know
which wait we need to use - if we use correct, our tests run very fast and not fails on click and similar actions.
https://www.selenium.dev/documentation/webdriver/waits/

If we want to understand why some functions fails, we need to understand concept of exceptions:
https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

Sometimes we need to modify such methods as "click_an_element" depending on exceptions.
"""

from typing import Union

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.customers_table import Customer_Table_Menu
from locators.locator_forms import SimpleLocatorForm
from methods.timer import Timer
from properties.config import TIMEOUT


class HelperMethods:
    """
    Selenium functions
    """

    def __init__(self, driver: webdriver, log):
        self.driver = driver
        self.log = log

    def open_page(self, url: str) -> None:
        """
        Opens page
        :param url: portal url
        :return: None
        """
        self.log.info("Opening WebPortal")
        self.driver.get(url)

    def locate_element(self, by_locator: tuple, timeout: int = TIMEOUT) -> Union[WebElement, None]:
        """
        Wait until element is visible and return it
        :param by_locator: locator
        :param timeout: waiting time for WEB element
        :return: WebElement or None
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(by_locator))
        except (TimeoutException, TypeError):
            return None
        return element

    def locate_elements(self, locator: tuple, timeout: int = TIMEOUT) -> list[WebElement]:
        """
        Wait until element is visible and return it
        :param locator: locator
        :param timeout: waiting time for WEB element
        :return: WebElement or None
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
        except (TimeoutException, NoSuchElementException) as element_not_found:
            raise TimeoutException("Elements not found") from element_not_found
        return elements

    def wait_until_element_clickable(self, by_locator: tuple, timeout: int = TIMEOUT) -> Union[WebElement, None]:
        """
        Waiting element until it's clickable
        :param by_locator: locator
        :param timeout: waiting time for WEB element
        :return: WebElement or None
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(by_locator))
        except TimeoutException:
            return None
        return element

    def do_click(self, field: SimpleLocatorForm, timeout=TIMEOUT) -> None:
        """
        Click element
        :param: field, timeout
        :return: None
        """
        element = self.wait_until_element_clickable(field.locator, timeout=timeout)
        if element:
            element.click()
            self.log.info(f"Clicks {field.name} button")
        else:
            self.log.warn(f"Button {field.name} click doesn't work")

    def do_send_keys(self, field: SimpleLocatorForm, text: [str, Keys], clear_data: bool = True) -> None:
        """
        Sends value to portal web element
        :param field: page field
        :param clear_data: clearing element's data
        :param text: text should be presented to element
        :return: None
        """
        element = self.locate_element(field.locator)
        if element:
            if clear_data:
                element.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
            element.send_keys(text)
            self.log.info(f'Text "{text}" send {field.name} to field.')
        else:
            self.log.warn(f'Text "{text}" could not be send to {field.name} field.')

    def get_element_css_property(self, field: SimpleLocatorForm, value: str):
        """
        Wait until element is located and get element css property
        :param field:
        :param value:
        :return:
        """
        element = self.locate_element(field.locator)
        return element.value_of_css_property(value)

    def wait_until_element_presented(self, field: SimpleLocatorForm) -> Union[WebElement, None]:
        """
        Wait until presence of element is located
        :param field:
        :return: WebElement or None
        """
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(field.locator))
        return element

    def move_to_element(self, field: SimpleLocatorForm) -> None:
        """
        Moves to invisible/untouchable element
        :param field:
        :return: None
        """
        self.log.info(f"Move cursor to {field.name}")
        web_element = self.wait_until_element_clickable(field.locator)
        ActionChains(self.driver).move_to_element(web_element).perform()

    def move_to_element_and_click(self, field: SimpleLocatorForm) -> None:
        """
        Moves to invisible/untouchable element and clicks it
        :param field:
        :return: none
        """
        self.log.info(f"Move cursor to {field.name} and click")
        web_element = self.wait_until_element_clickable(field.locator)
        ActionChains(self.driver).move_to_element(web_element).click().perform()

    def is_displayed(self, field: SimpleLocatorForm, timeout: int = TIMEOUT) -> bool:
        """
        Check if element is displayed
        :param field: browser element
        :param timeout: waiting time
        :return: True or False
        """
        element = self.locate_element(by_locator=field.locator, timeout=timeout)
        display = bool(element.is_displayed())
        self.log.info(f'Element "{field.name}" is displayed: {display}')
        return display

    def slide_element(self, by_locator, x_offset, y_offset) -> None:
        """
        Moves to element ar drags into described position
        :param by_locator:
        :param x_offset:
        :param y_offset:
        :return: None
        """
        element = self.driver.find_element(By.XPATH, by_locator)
        ActionChains(self.driver).drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    def drag_and_drop(self, drag_element: Customer_Table_Menu, drop_element: Customer_Table_Menu) -> None:
        """
        Moves drags and drops element into described position by xpath
        :param drag_element: colum
        :param drop_element:
        :return: None
        """
        self.log.info(f"Drag {drag_element.name} and drop to {drop_element.name}")
        drag = self.wait_until_element_clickable(drag_element.six_dots_locator)
        drop = self.wait_until_element_clickable(drop_element.six_dots_locator)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    def get_text_from_element(self, field: SimpleLocatorForm) -> Union[str, None]:
        """
        gets text from Element
        :param field: field in web page
        :return: element text or None
        """
        element = self.locate_element(by_locator=field.locator)
        if element:
            self.log.info(f"Element's {field.name}'s value: {element.text}")
            return element.text
        self.log.info(f"Element {field.name} is None and doesn't contain value")
        return None

    def get_text_from_elements(self, field: SimpleLocatorForm, timeout=TIMEOUT) -> list[str]:
        """
        gets text from Elements
        :param field: field in web page
        :param timeout: waiting time
        :return: element text or None
        """
        result = []
        elements = self.locate_elements(field.locator, timeout=timeout)
        for element in elements:
            result.append(element.text)
        self.log.info(f'Fields {field.name} has text in element: {result}')
        return result

    def wait_until_element_disappear(self, field: SimpleLocatorForm, timeout=TIMEOUT) -> bool:
        """
        Function waits until disappear element
        :param field: field, which should be checked
        :param timeout: max time for looking element
        :return: exists element or not after checking time. Function stop looking when don't see such element
        """
        self.log.info(f'looking for {field.name} element')
        timer = Timer(timeout=timeout)
        while not timer.fired():
            if self.locate_element(by_locator=field.locator, timeout=1) is None:
                self.log.info('Element not found')
                return True
        self.log.warn('Element still exists')
        return False
