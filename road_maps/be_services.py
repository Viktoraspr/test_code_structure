"""
Here we keep all road points, which need to be checked by API tests

In other words, here I have all endpoints, which should be checked.
"""
from data_for_tests.data_for_tests import CUSTOMER_DEFAULT


class RoadMap:
    """
    Class for all roadmap endpoints
    """
    SWAGGER_URL = 'Here_we_have_swagger_url'

    def __init__(self):
        self.customer_resource = f'{self.SWAGGER_URL}customers/v1/'
        self.customer_resource_company_logo = self.SWAGGER_URL + '{customer-id}/company-logo'

        self.calc_toll_resource = f'{self.SWAGGER_URL}calc-tolls/v1'

        self.transaction_resource = f'{self.SWAGGER_URL}transactions/v1/'
        self.transaction_resource_generate = f'{self.transaction_resource}generate'
        self.transaction_resource_math = f'{self.transaction_resource}match'
        self.transaction_resource_upload_csv = f'{self.transaction_resource}upload/csv'
        self.transaction_resource_upload_xlsx = f'{self.transaction_resource}upload/xlsw'

        self.trips_resource = f'{self.SWAGGER_URL}trips/v1/'
        self.trips_resource_alternative = self.trips_resource + '{}alternative-trip'
        self.trips_resource_original = self.trips_resource + '{}original-trip'

        self.roles_resource = f'{self.SWAGGER_URL}roles/v1/'
        self.users_resource = f'{self.SWAGGER_URL}users/v1/'

        self.agencies_resource = f'{self.SWAGGER_URL}lists/v1/agencies/'
        self.tag_types_resource = f'{self.SWAGGER_URL}lists/v1/tag-types/'
        self.vehicle_classes_resource = f'{self.SWAGGER_URL}lists/v1/tag-types/'

        self.vehicles_resource = f'{self.SWAGGER_URL}vehicles/v1/'
        self.vehicles_resource_validate = f'{self.SWAGGER_URL}vehicles/v1/validate'

    def get_list_of_endpoints_for_checking_with_get_method_positive_tests(self) -> list[tuple]:
        """
        Function for endpoints for checking with get method.
        :return: list of end point must be checked by get method
        """
        checking_end_points = [
            (self.customer_resource,),
            (self.transaction_resource, {'customer-id': CUSTOMER_DEFAULT.user}),
            (self.trips_resource, {'customer-id': CUSTOMER_DEFAULT.user}),
            (self.roles_resource,),
            (self.users_resource, {'customer-id': CUSTOMER_DEFAULT.user}),
            (self.agencies_resource,),
            (self.tag_types_resource,),
            (self.vehicle_classes_resource,),
            (self.vehicles_resource, {'customer-id': CUSTOMER_DEFAULT.user}),
            (self.vehicles_resource_validate, {'customer-id': CUSTOMER_DEFAULT.user})
        ]
        return checking_end_points

    def get_list_of_endpoints_for_checking_with_get_method_negative_tests(self) -> list[tuple]:
        """
        Function for endpoints for checking with get method.
        :return: list of end point must be checked by get method
        """
        checking_end_points = [
            (self.transaction_resource,),
            (self.calc_toll_resource,),
            (self.trips_resource,),
            (self.users_resource,),
            (self.vehicles_resource,),
        ]
        return checking_end_points
