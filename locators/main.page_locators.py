"""
All locators before login.
"""

from selenium.webdriver.common.by import By

from locators.locator_forms import SimpleLocatorForm


class WebPortalHomePage():
    """
    All locators before login.
    """
    login_button = SimpleLocatorForm(name="Login button",
                                     locator=(By.XPATH, "//a[text()='Log In']"))
    contact_us_button = SimpleLocatorForm(name="Contact us button",
                                          locator=(By.XPATH, "//a[text()='Contact Us']"))
    slogan = SimpleLocatorForm(name="Connecting logic and motion...",
                               locator=(By.XPATH, "//p[text()='Connecting logic and motion...']"))
    contact_us_container = SimpleLocatorForm(
        name="Contact Us", locator=(By.XPATH, "//p[text()='Contact Us']/ancestor::div[@class='left-column']"))
    visit_us_container = SimpleLocatorForm(name='Visit',
                                           locator=(By.XPATH, "//div[@class='visit']"))
    get_in_touch_container = SimpleLocatorForm(name='Contacts',
                                               locator=(By.XPATH, "//div[@class='contacts']"))
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
