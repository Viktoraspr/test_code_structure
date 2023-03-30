import datetime
from typing import Union

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from locators.locator_forms import SimpleLocatorForm
from methods.helper_selenium_methods import HelperMethods
from data_for_tests.data_dataclass_forms import Agency, TRA


class OctopusPage(HelperMethods):
    # UI objects with selector
    choose_agency_name_drop_list = SimpleLocatorForm(name="Choose Agency Name list", locator=(
        By.XPATH, "//label[text()='Agency Name']/following-sibling::div"
                  "/span[contains(@class, 'select-input-content_container')]"))
    view_vehicle_class_button = SimpleLocatorForm(name="View Vehicle Class",
                                                  locator=(By.XPATH, "//button[text()='View vehicle class']"))
    add_new_agency_button = SimpleLocatorForm(name="Add New Agency button",
                                              locator=(By.XPATH, "//button[text()='Add new agency']"))
    button_save = SimpleLocatorForm(name="Save", locator=(By.XPATH, "//button[text()='Save']"))
    state_field = SimpleLocatorForm(name="State", locator=(By.XPATH, "//input[@id='stateName']"))
    agency_field = SimpleLocatorForm(name="Agency", locator=(By.XPATH, "//input[@id='name']"))
    state_field_error = SimpleLocatorForm(name="State field error",
                                          locator=(By.XPATH, "//span[text()='stateName is a required field']"))
    agency_field_error = SimpleLocatorForm(name="Agency field error",
                                           locator=(By.XPATH, "//span[text()='name is a required field']"))
    delete_agency_button = SimpleLocatorForm(name="Delete Agency button",
                                             locator=(By.XPATH, "//button[text()='Delete agency']"))
    delete_agency_confirm_field = SimpleLocatorForm(name="Confirm", locator=(By.XPATH, "//input[@id='confirm']"))
    delete_agency_empty_field_error = SimpleLocatorForm(name="Delete agency empty filed error", locator=(
        By.XPATH, "//span[text()='confirm is a required field']"))
    delete_agency_field_wrong_text_error = SimpleLocatorForm(name="Delete agency field wrong text error",
                                                             locator=(By.XPATH, "//span[text()='Uncorrect input']"))
    delete_button = SimpleLocatorForm(name="Delete", locator=(By.XPATH, "//button[text()='Delete']"))
    pop_up_delete_button = SimpleLocatorForm(name="Pop up delete button",
                                             locator=(By.XPATH, "//button[@type='submit' and text()='Delete']"))
    agency_search_field = SimpleLocatorForm(name="Agency search", locator=(By.XPATH, "//input[@id='search-input']"))
    add_new_tra_button = SimpleLocatorForm(name="Add New TRA",
                                           locator=(By.XPATH, "//button[text()='Add new TRA']"))
    description_field = SimpleLocatorForm(name="Description", locator=(By.XPATH, "//input[@id='description']"))
    latitude_field = SimpleLocatorForm(name="Latitude", locator=(By.XPATH, "//input[@id='latitude']"))
    longitude_field = SimpleLocatorForm(name="Longitude", locator=(By.XPATH, "//input[@id='longitude']"))
    description_field_error = SimpleLocatorForm(name="Description field error",
                                                locator=(By.XPATH, "//span[text()='description is a required field']"))
    latitude_field_error = SimpleLocatorForm(name="Latitude field error",
                                             locator=(By.XPATH, "//span[text()='latitude is a required field']"))
    longitude_field_error = SimpleLocatorForm(name="Longitude field error",
                                              locator=(By.XPATH, "//span[text()='longitude is a required field']"))
    agency_container = SimpleLocatorForm(name="Agency container", locator=(By.CLASS_NAME, "popover_list__G8qfa"))
    tra_container = SimpleLocatorForm(name="TRA container", locator=(By.CLASS_NAME, "CardContainer_container__GaTpX"))
    vehicle_class_container = SimpleLocatorForm(name="Vehicle class container",
                                                locator=(By.CLASS_NAME, "Table_container__YmQNy"))
    add_new_tda_button = SimpleLocatorForm(name="Add New TDA",
                                           locator=(By.XPATH, "//button[text()='Add new TDA']"))
    wide_area_field = SimpleLocatorForm(name="Wide Area", locator=(By.XPATH, "//input[@id='wide_area']"))
    nearby_area_field = SimpleLocatorForm(name="Nearby Area", locator=(By.XPATH, "//input[@id='nearby_area']"))
    wide_area_field_error = SimpleLocatorForm(name="Wide area field error",
                                              locator=(By.XPATH, "//span[text()='wide_area is a required field']"))
    nearby_area_field_error = SimpleLocatorForm(name="Nearby area field error",
                                                locator=(By.XPATH, "//span[text()='nearby_area is a required field']"))
    tda_container = SimpleLocatorForm(name="TDA container",
                                      locator=(By.XPATH, "//div[@class='accordion_content__vHgV+']"))
    cancel_button = SimpleLocatorForm(name="Cancel", locator=(By.XPATH, "//button[text()='Cancel']"))
    add_new_rate_class_button = SimpleLocatorForm(name="Add New Rate Class button",
                                                  locator=(By.XPATH, "//button[text()='Add new rate class']"))
    agency_class_name_field = SimpleLocatorForm(name="Agency Class Name",
                                                locator=(By.XPATH, "//input[@id='agency_class']"))
    agency_class_name_field_required_error = SimpleLocatorForm(name="Agency class name requred error", locator=(
        By.XPATH, "//span[text()='agency_class is a required field']"))
    agency_class_name_duplicate_error = SimpleLocatorForm(name="agency classanmeduplicate error", locator=(
        By.XPATH, "//span[text()='There is class with the same name. "
                  "Please, change it']"))
    vehicle_type_field = SimpleLocatorForm(name="Vehicle type",
                                           locator=(By.XPATH, "//label[text()='Vehicle type']/following-sibling::div"))
    clear_vehicle_class_button = SimpleLocatorForm(name="Clear Vehicle Class", locator=(
        By.XPATH, "//span[contains(@class, 'select-input-icons_clear')]"))
    button_view_rates = SimpleLocatorForm(name="View Rates button", locator=(By.XPATH, "//button[text()='View rates']"))
    button_add_new_toll_rate = SimpleLocatorForm(name="Add New Toll Rate",
                                                 locator=(By.XPATH, "//button[text()='Add new toll rate']"))
    rate_class_error = SimpleLocatorForm(name="Rate class error",
                                         locator=(By.XPATH, "//span[text()='rate_class is a required field']"))
    toll_amount_error = SimpleLocatorForm(name="Toll amount error",
                                          locator=(By.XPATH, "//span[text()='toll_amount is a required field']"))
    payment_type_error = SimpleLocatorForm(name="Payment type error",
                                           locator=(By.XPATH, "//span[text()='payment_type is a required field']"))
    toll_rates_container = SimpleLocatorForm(name="Toll rates container",
                                             locator=(By.XPATH, "//*[@class='Table_container__YmQNy']"))
    rate_class_field = SimpleLocatorForm(name="Rate Class",
                                         locator=(By.XPATH, "//label[@for='Rate class']/following-sibling::div"))
    toll_amount_field = SimpleLocatorForm(name="Toll Amount", locator=(By.XPATH, "//input[@id='toll_amount']"))
    payment_type_field = SimpleLocatorForm(name="Payment Type",
                                           locator=(By.XPATH, "//label[@for='Payment type']/following-sibling::div"))
    start_date_field = SimpleLocatorForm(name="Start Date", locator=(
        By.XPATH, "//label[@for='Start validity of the rate']/following-sibling::div"))
    end_date_field = SimpleLocatorForm(name="End Date", locator=(
        By.XPATH, "//label[@for='End validity of the rate']/following-sibling::div"))
    today_date = SimpleLocatorForm(name="Today Date", locator=(
        By.XPATH, "//div[@class='react-datepicker__week']/div[@aria-selected='true']"))
    week_after_current_day = SimpleLocatorForm(name="Week after current day",
                                               locator=(By.XPATH, "//div[@class='react-datepicker__week']"
                                                                  "/div[@aria-selected='true']/parent::div/following-sibling::div[1]/div[7]"))
    next_year = SimpleLocatorForm(name="Next year", locator=(By.XPATH,
                                                             "//button[@class='select-popover-items_container__-"
                                                             "WqS4 select-popover-items_selected__o2L9N "
                                                             "undefined']/following-sibling::button[1]"))
    year_picker = SimpleLocatorForm(name="Year picker",
                                    locator=(By.XPATH, "//div[@class='custom-header_container__40FEG']/div[2]"))
    start_date_error = SimpleLocatorForm(name="Start date error",
                                         locator=(By.XPATH, "//span[text()='start_date is a required field']"))
    end_date_error = SimpleLocatorForm(name="end date error",
                                       locator=(By.XPATH, "//span[text()='end_date is a required field']"))
    delete_tra_button = SimpleLocatorForm(name="Delete TRA",
                                          locator=(By.XPATH, "//button[@data-button-label='delete-tra']"))
    edit_tra_button = SimpleLocatorForm(name="Edit TRA",
                                        locator=(By.XPATH, "//button[@data-button-label='edit-tra']"))
    tda_element = SimpleLocatorForm(name="TDA",
                                    locator=(By.XPATH, "//div[@class='TDACard_container__7-9wl']/h3[@role='button']"))
    edit_tda_button = SimpleLocatorForm(name="Edit TDA",
                                        locator=(By.XPATH, "//button[@data-button-label='edit-tda']"))
    delete_tda_button = SimpleLocatorForm(name="Delete TDA button",
                                          locator=(By.XPATH, "//button[@data-button-label='delete-tda']"))
    search_bar = SimpleLocatorForm(name="Search bar", locator=(By.XPATH, "//input[@placeholder]"))
    without_max_value_checkbox = SimpleLocatorForm(name="Without max value checkbox",
                                                   locator=(By.XPATH, "(//span[text()='Without max value'])"))
    infinity_max_value_checkbox = SimpleLocatorForm(name="Infinity max value checkbox",
                                                    locator=(By.XPATH, "(//span[text()='Infinity max value'])"))
    agency_element = SimpleLocatorForm(name="Agency", locator=(
        By.XPATH, "//button[@class='select-popover-items_container__-WqS4 undefined']"))
    tra_element = SimpleLocatorForm(name="TRA", locator=(By.XPATH, "//div[@class='TRACardContent_content__SgXB9']/h2"))
    tra_id_element = SimpleLocatorForm(name="TRA id",
                                       locator=(By.XPATH, "//div[@class='TRACardContent_id_row__o8EHc']/p"))
    vehicle_class_element = SimpleLocatorForm(name="Vehicle class",
                                              locator=(By.XPATH, "//div[@class='TableRow_container__2ZGeq']/div[1]"))
    vehicle_type_pop_up = SimpleLocatorForm(name="Vehicle type pop up",
                                            locator=(By.XPATH, "//ul[@class='popover_list__G8qfa']/button"))
    rate_class_pop_up = SimpleLocatorForm(name="Rate class pop up",
                                          locator=(By.XPATH, "//ul[@class='popover_list__G8qfa']/button"))
    toll_amount_value = SimpleLocatorForm(name="Toll amount value",
                                          locator=(By.XPATH, "//div[@class='TableItem_container__HVhIk'][2]"))

    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.log = log

    @staticmethod
    def get_next_year_date():
        """
        Returns xpath expression of year date from current date
        :return: None
        """
        today_date = datetime.date.today().day
        return "//div[text()='" + str(today_date) + "']"

    def click_cross(self, pop_up_name: str):
        """
        Closes following pop-up window
        :param pop_up_name: str
        :return: None
        """
        cross_element = SimpleLocatorForm(name=pop_up_name + " pop up cross", locator=(
            By.XPATH, "//h3[text()='" + pop_up_name + "']/parent::section/following-sibling::button"))
        self.do_click(cross_element)

    def select_agency(self, agency: str):
        """
        Selects Agency from the list
        :param agency: str
        :return: None
        """
        agency_element = SimpleLocatorForm(name=agency, locator=(By.XPATH, "//button[text()='" + agency + "']"))
        self.do_click(self.choose_agency_name_drop_list)
        self.do_click(agency_element)

    def add_new_agency(self, data: Agency):
        """
        Adds new agency
        :param data:
        :return: None
        """
        self.do_click(self.add_new_agency_button)
        self.do_send_keys(self.state_field, data.state)
        self.do_send_keys(self.agency_field, data.agency_name)
        self.do_click(self.button_save)

    def delete_agency(self, agency: str, agency_selected: str):
        """
        Deletes Agency
        :param agency: str
        :param agency_selected: str
        :return: None
        """
        agency_element = SimpleLocatorForm(name=agency, locator=(By.XPATH, "//button[text()='" + agency + "']"))
        if agency_selected is False:
            if not self.is_displayed(self.agency_search_field):
                self.do_click(self.choose_agency_name_drop_list)
            self.do_click(agency_element)
            self.do_click(self.delete_agency_button)
            self.do_send_keys(self.delete_agency_confirm_field, "DELETE AGENCY")
            self.do_click(self.delete_button)
        else:
            self.do_click(self.delete_agency_button)
            self.do_send_keys(self.delete_agency_confirm_field, "DELETE AGENCY")
            self.do_click(self.delete_button)

    def retrieve_agency_list(self) -> list[str]:
        """
        Retrieves list of Agencies
        :return: list[str]
        """
        agency_list = []
        locator, xpath = self.agency_element
        self.do_click(self.choose_agency_name_drop_list)
        try:
            parent_obj = self.wait_until_element_presented(self.agency_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    agency_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return agency_list

    def retrieve_tra_points(self) -> list[str]:
        """
        Retrieves list of Agency TRAs
        :return: list[str]
        """
        tra_list = []
        locator, xpath = self.tra_element
        try:
            parent_obj = self.wait_until_element_presented(self.tra_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    tra_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return tra_list

    def retrieve_tra_point_ids(self) -> list[str]:
        """
        Retrieves list of Agency TRA ID's
        :return: list[str]
        """
        id_list = []
        locator, xpath = self.tra_id_element
        try:
            parent_obj = self.wait_until_element_presented(self.tra_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    id_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return id_list

    def select_tra_action(self, tra_name, xpath_action):
        """
        Selects whether Delete or Edit TRA
        :param tra_name: str
        :param xpath_action: SimpleLocatorForm
        :return: None
        """
        element = SimpleLocatorForm(name=tra_name, locator=(By.XPATH, "(//div[@class='TRACardContent_content__SgXB9']"
                                                                      "/h2[text()='" + tra_name + "']/parent::div/following-sibling::div)"))
        # locator, xpath = element
        # self.locate_element(element)
        self.move_to_element(element)
        self.move_to_element_and_click(xpath_action)

    def delete_tra(self, tra_name):
        """
        Deletes TRA
        :param tra_name: str
        :return: None
        """
        element = SimpleLocatorForm(name=tra_name, locator=(By.XPATH, "(//div[@class='TRACardContent_content__SgXB9']"
                                                                      "/h2[text()='" + tra_name + "']/parent::div/following-sibling::div)"))
        self.move_to_element(element)
        self.move_to_element_and_click(self.delete_tra_button)
        self.do_click(self.delete_button)

    def add_new_tra(self, data: TRA):
        """
        Adds new TRA
        :param data:
        :return: None
        """
        self.do_click(self.add_new_tra_button)
        self.do_send_keys(self.description_field, data.description)
        self.do_send_keys(self.latitude_field, data.latitude)
        self.do_send_keys(self.longitude_field, data.longitude)
        self.do_click(self.button_save)

    def edit_tra(self, tra_name, description, latitude, longitude):
        """
        Edits created TRA
        :param tra_name: str
        :param description: str
        :param latitude: str
        :param longitude: str
        :return: None
        """
        self.select_tra_action(tra_name, self.edit_tra_button)
        self.do_send_keys(self.description_field, description)
        self.do_send_keys(self.latitude_field, latitude)
        self.do_send_keys(self.longitude_field, longitude)
        self.do_click(self.button_save)

    def expand_collapse_tra(self, tra_name):
        """
        Expands or collapses TRA
        :param tra_name: str
        :return: None
        """
        tra_element = SimpleLocatorForm(name=tra_name,
                                        locator=(By.XPATH, "//div[@class='TRACardContent_content__SgXB9']"
                                                           "/h2[text()='" + tra_name + "']"
                                                        "/parent::div/parent::div/preceding-sibling::section"
                                                        "//span[@class='accordion_icon__6zF+E']"))
        count = 0
        succeed = False
        while not succeed and count < 6:
            try:
                self.wait_until_element_clickable(tra_element)
                self.do_click(tra_element)
                succeed = True
            except StaleElementReferenceException:
                pass

    def retrieve_tda_list(self) -> list[str]:
        """
        Retrieves list of TRAs TDAs
        :return: list[str]
        """
        tda_list = []
        locator, xpath = self.tda_element
        try:
            parent_obj = self.wait_until_element_presented(self.tda_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    tda_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return tda_list

    def add_new_tda(self, wide_area, nearby_area, latitude, longitude):
        """
        Adds new TDA
        :param wide_area: str
        :param nearby_area:str
        :param latitude: str
        :param longitude: str
        :return: None
        """
        self.do_click(self.add_new_tda_button)
        self.do_send_keys(self.wide_area_field, wide_area)
        self.do_send_keys(self.nearby_area_field, nearby_area)
        self.do_send_keys(self.latitude_field, latitude)
        self.do_send_keys(self.longitude_field, longitude)
        self.do_click(self.button_save)

    def click_edit_tda(self, tda_container):
        """
        Clicks edit TDA
        :param tda_container:
        :return: None
        """
        locator, xpath = self.tda_element
        element = locator, xpath + tda_container
        self.move_to_element(element)
        self.move_to_element_and_click(self.edit_tda_button)

    def select_tda_type(self, previous_tda_type, new_tda_type):
        """
        Selects TDA type
        :param previous_tda_type: SimpleLocatorForm
        :param new_tda_type: SimpleLocatorForm
        :return: None
        """
        previous_tda_element = SimpleLocatorForm(name=previous_tda_type,
                                                 locator=(By.XPATH, "//span[text()='" + previous_tda_type + "']"))
        new_tda_element = SimpleLocatorForm(name=new_tda_type,
                                            locator=(By.XPATH, "//button[text()='" + new_tda_type + "']"))
        self.do_click(previous_tda_element)
        self.do_click(new_tda_element)

    def tda_type_field(self, tda_type) -> Union[WebElement, None]:
        """
        TDA type field
        :param tda_type:
        :return: WebElement
        """
        tda_type_element = (By.XPATH, "//span[text()='" + tda_type + "']")
        return self.locate_element(tda_type_element)

    def edit_tda(self, tda_container, previous_tda_type, new_tda_element, nearby_area, latitude, longitude):
        """
        Edits created TDA
        :param tda_container: str
        :param previous_tda_type: str
        :param new_tda_element: str
        :param nearby_area: str
        :param latitude: str
        :param longitude: str
        :return: None
        """
        self.click_edit_tda(tda_container)
        self.select_tda_type(previous_tda_type, new_tda_element)
        self.do_send_keys(self.nearby_area_field, nearby_area)
        self.do_send_keys(self.latitude_field, latitude)
        self.do_send_keys(self.longitude_field, longitude)
        self.do_click(self.button_save)

    def delete_tda(self, tda_container):
        """
        Deletes TDA
        :param tda_container: str
        :return: None
        """
        locator, xpath = self.tda_element
        element = locator, xpath + tda_container
        self.move_to_element(element)
        self.move_to_element_and_click(self.delete_tda_button)
        self.do_click(self.delete_button)

    def retrieve_vehicle_class_list(self) -> list[str]:
        """
        Retrieves list of Agency Vehicle classes
        :return: list[str]
        """
        vehicle_class_list = []
        locator, xpath = self.vehicle_class_element
        try:
            parent_obj = self.wait_until_element_presented(self.vehicle_class_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    vehicle_class_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return vehicle_class_list

    def select_vehicle_type(self, vehicle_type_option):
        """
        Selects vehicle type
        :param vehicle_type_option:
        :return: None
        """
        locator, xpath = self.vehicle_type_pop_up
        vehicle_type_select = locator, xpath + vehicle_type_option
        self.do_click(self.vehicle_type_field)
        self.do_click(vehicle_type_select)

    def click_edit_vehicle_class(self, vehicle_class_name):
        """
        Clicks edit vehicle class by name
        :param vehicle_class_name: str
        :return: None
        """
        vehicle_class_element = SimpleLocatorForm(name=vehicle_class_name, locator=(By.XPATH,
                                                                                    "//div[text()='" + vehicle_class_name + "']"
                                                                                                                            "/following-sibling::div[contains(@class, 'TableItem_icon__NbC1y')]"))
        self.do_click(vehicle_class_element)

    def return_vehicle_class_field_text(self, vehicle_class_name, field) -> str:
        """
        Returns vehicle class field values
        :param vehicle_class_name: str
        :param field: str
        :return: str
        """
        container = ""
        list_of_fields = ["VEHICLE TYPE", "WEIGHT", "HEIGHT", "VEHICLE AXLES", "VEHICLE TIRES"]
        try:
            if field in list_of_fields:
                container = "[" + str(list_of_fields.index(field) + 1) + "]"
        except Exception as e:
            self.log.error("Vehicle Class name or vehicle class not found.\n", e)
        field_element = (By.XPATH, "//div[text()='" + field + "']"
                                                              "/parent::div/following-sibling::div"
                                                              "//div[text()='" + vehicle_class_name + "']"
                                                                                                      "/following-sibling::div" + container)
        return self.locate_element(field_element).text

    def define_slider_input(self, slider_input_name, without_checkbox_state, infinity_checkbox_state, slider_x_offset,
                            slider_y_offset):
        """
        Selects slider input in vehicle class creation and defines with values
        :param slider_input_name: str
        :param without_checkbox_state: str
        :param infinity_checkbox_state: str
        :param slider_x_offset: str
        :param slider_y_offset: str
        :return: None
        """
        checkbox_container = ""
        list_of_slider_input = ["Weight", "Height", "Vehicle Axles", "Vehicle Tires"]
        try:
            if slider_input_name in list_of_slider_input:
                checkbox_container = "[" + str(list_of_slider_input.index(slider_input_name) + 1) + "]"
        except Exception as e:
            self.log.error("Wrong Slider input name or slider input not found.\n", e)
        elem_one_locator, elem_one_xpath = self.without_max_value_checkbox
        elem_two_locator, elem_two_xpath = self.infinity_max_value_checkbox
        without_checkbox_element = elem_one_locator, elem_one_xpath + checkbox_container
        infinity_checkbox_element = elem_two_locator, elem_two_xpath + checkbox_container
        slider_element = "//label[contains(text(), '" + slider_input_name + "')]" \
                                                                            "/following-sibling::div//span[@class='slider_range__GUYzU']"
        if without_checkbox_state is True:
            self.do_click(without_checkbox_element)
            self.slide_element(slider_element, slider_x_offset, slider_y_offset)
        elif infinity_checkbox_state is True:
            self.do_click(infinity_checkbox_element)
            self.slide_element(slider_element, slider_x_offset, slider_x_offset)
        else:
            self.slide_element(slider_element, slider_x_offset, slider_x_offset)

    def select_rate_class(self, rate_class_option):
        """
        Selects rate class
        :param rate_class_option:
        :return: None
        """
        if rate_class_option is not None:
            locator, xpath = self.rate_class_pop_up
            rate_class_select = (locator, xpath + rate_class_option)
            self.do_click(self.rate_class_field)
            self.do_click(rate_class_select)

    def select_payment_type(self, payment_type_option):
        """
        Selects payment type
        :param payment_type_option:
        :return: None
        """
        if payment_type_option is not None:
            locator, xpath = self.rate_class_pop_up
            payment_type_select = (locator, xpath + payment_type_option)
            self.do_click(self.payment_type_field)
            self.do_click(payment_type_select)

    def select_date(self, date_type, date, year):
        """
        Selects validity date
        :param date_type:
        :param date:
        :param year:
        :return:
        """
        if date_type and date is not None:
            self.do_click(date_type)
            if year is not None:
                self.do_click(self.year_picker)
                self.do_click(year)
            self.do_click(date)

    def add_new_toll_rate(self, rate_class, toll_amount, payment_type, start_date, end_date):
        """
        Adds new Toll rate
        :param rate_class: str
        :param toll_amount: str
        :param payment_type: str
        :param start_date: str
        :param end_date: str
        :return: None
        """
        self.select_rate_class(rate_class)
        self.do_send_keys(self.toll_amount_field, toll_amount)
        self.select_payment_type(payment_type)
        if start_date is not None:
            self.select_date(self.start_date_field, self.today_date, None)
        if end_date is not None:
            self.select_date(self.end_date_field, (By.XPATH, self.get_next_year_date()), self.next_year)

    def return_rate_class_field_text(self, rate_class_name, field) -> str:
        """
        Returns rate class field values
        :param rate_class_name:
        :param field:
        :return: list[str]
        """
        container = ""
        list_of_fields = ["TOLL AMOUNT", "PAYMENT TYPE", "START VALIDITY", "END VALIDITY"]
        try:
            if field in list_of_fields:
                container = "[" + str(list_of_fields.index(field) + 1) + "]"
        except Exception as e:
            self.log.error("Rate Class name or rate class not found.\n", e)
        field_element = (By.XPATH, "//div[text()='" + field + "']"
                                                              "/parent::div/following-sibling::div//div[text()='" + rate_class_name + "']"
                                                                                                                                      "/following-sibling::div" + container)
        return self.locate_element(field_element).text

    def retrieve_toll_rates_list(self) -> list[str]:
        """
        Retrieves list of Toll Rates
        :return: list[str]
        """
        toll_rates_list = []
        locator, xpath = self.toll_amount_value
        try:
            parent_obj = self.wait_until_element_presented(self.toll_rates_container)
            try:
                container = parent_obj.find_elements(locator, xpath)
                for element in container:
                    toll_rates_list.append(element.text)
            except NoSuchElementException:
                self.log.error("Child element not found.")
        except NoSuchElementException:
            self.log.error("Parent element not found.")
        return toll_rates_list

    def edit_toll_rate(self, toll_amount, edited_toll_amount, payment_type):
        """
        Edits created toll rate
        :param toll_amount:
        :param edited_toll_amount:
        :param payment_type:
        :return: None
        """
        self.click_edit_toll_rate_button(toll_amount)
        self.do_send_keys(self.toll_amount_field, edited_toll_amount)
        self.select_payment_type(payment_type)
        self.select_date(self.start_date_field, self.today_date, None)

    def click_edit_toll_rate_button(self, toll_amount):
        """
        Clicks edit toll rate button by toll amount
        :param toll_amount:
        :return: None
        """
        edit_button = SimpleLocatorForm(name=toll_amount, locator=(By.XPATH, "//div[text()='" + toll_amount + "']"
                                                                                                              "/following-sibling::div[@class='TableItem_container__HVhIk TableItem_icon__NbC1y']"))
        self.do_click(edit_button)
