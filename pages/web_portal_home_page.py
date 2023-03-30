from selenium.webdriver.common.by import By

from locators.locator_forms import SimpleLocatorForm
from methods.helper_selenium_methods import HelperMethods
from data_for_tests.data_dataclass_forms import MessageData


class WebPortalHomePage(HelperMethods):
    """
    User interface objects with selector
    """
    login_button = SimpleLocatorForm(name="Login button",
                                     locator=(By.XPATH, "//a[text()='Log In']"))
    contact_us_button_first = SimpleLocatorForm(name='Contact us button',
                                                locator=(By.XPATH, '//li[@class="menu-item"]'))
    contact_us_button_second = SimpleLocatorForm(name="Contact us button",
                                                 locator=(By.XPATH, "//a[text()='Contact Us']"))
    slogan = SimpleLocatorForm(name="Connecting logic and motion...",
                               locator=(By.XPATH, "//p[text()='Connecting logic and motion...']"))
    commerce_logic = SimpleLocatorForm(name='commercelogic',
                                       locator=(By.XPATH, '/html/body/div/header/div/span[1]'))
    contact_us_container = SimpleLocatorForm(
        name="Contact Us", locator=(By.XPATH, "//p[text()='Contact Us']/ancestor::div[@class='left-column']"))
    visit_us_container = SimpleLocatorForm(name='Visit',
                                           locator=(By.XPATH, "//div[@class='visit']"))
    get_in_touch_container = SimpleLocatorForm(name='Contacts',
                                               locator=(By.XPATH, "//div[@class='contacts']"))
    map_container = SimpleLocatorForm(name='Map',
                                      locator=(By.XPATH, '//div[@class="map"]'))
    name_field = SimpleLocatorForm(name='Name',
                                   locator=(By.XPATH, "//input[@id='username']"))
    organization_field = SimpleLocatorForm(name='Organization',
                                           locator=(By.XPATH, "//input[@id='organization']"))
    email_field = SimpleLocatorForm(name='Email',
                                    locator=(By.XPATH, "//input[@id='email']"))
    phone_field = SimpleLocatorForm(name='Phone',
                                    locator=(By.XPATH, "//input[@id='phone']"))
    message_field = SimpleLocatorForm(name='Message',
                                      locator=(By.XPATH, "//textarea[@id='message']"))
    send_message_button = SimpleLocatorForm(name='Send Message',
                                            locator=(By.XPATH, "//button[text()='Send Message']"))
    successful_message = SimpleLocatorForm(name='Successful message',
                                           locator=(By.XPATH, "//div[@class='messagebox show']"))
    container_error = SimpleLocatorForm(name='Container error',
                                        locator=(By.XPATH, '//div[@class="container error"]'))
    message_error = SimpleLocatorForm(name='Message Error',
                                      locator=(By.XPATH, '//div[@class="areabox error"]'))

    def send_message(self, data: MessageData) -> None:
        """
        Sends message in "Contact Us" area
        :return: None
        """
        self.do_send_keys(self.name_field, data.name)
        self.do_send_keys(self.organization_field, data.organization)
        self.do_send_keys(self.email_field, data.email)
        self.do_send_keys(self.phone_field, data.phone)
        self.do_send_keys(self.message_field, data.message)
        self.do_click(self.send_message_button)
