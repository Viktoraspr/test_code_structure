"""
Endpoints tests
"""
import json
import unittest

import pytest
from parameterized import parameterized

from methods.database_methods import DatabaseMethods
from methods.rest_methods import RestMethods
from properties.config import TestData
from data_for_tests.data_for_tests import NEW_CUSTOMER_FOR_API_TESTS, NEW_USER_FOR_API_TESTS, NEW_VEHICLE_FOR_API_TESTS, \
    CUSTOMER_DEFAULT
from properties.logs import Logger
from users.users import DB_QA_USER
from road_maps.be_services import RoadMap

SQL_QUERIES = {
    f''' 
    delete from customer
    where company_name = '{NEW_CUSTOMER_FOR_API_TESTS['companyName']}';
            ''',
    f''' 
    delete from "user"
    where name = '{NEW_VEHICLE_FOR_API_TESTS['name']}';
    '''
}


class BeServices(unittest.TestCase):
    log = Logger().logger
    rest_method = RestMethods(log=log)
    headers = TestData.toll_guru_aws_headers

    @classmethod
    def setUpClass(cls):
        for sql_query in SQL_QUERIES:
            DatabaseMethods(user=DB_QA_USER, log=cls.log).delete_row_from_database(sql_query=sql_query)

    @classmethod
    def tearDownClass(cls):
        for sql_query in SQL_QUERIES:
            DatabaseMethods(user=DB_QA_USER, log=cls.log).delete_row_from_database(sql_query=sql_query)

    @pytest.mark.regression
    @parameterized.expand(RoadMap().get_list_of_endpoints_for_checking_with_get_method_positive_tests())
    def test_no_01_get_all_rows(self, url: str, params=None) -> None:
        """
        Test checks if endpoint work for API request.
        param url: url, which should be checked
        :param params: params for get method
        :return: None
        """
        requests = self.rest_method.get_request(url=url, params=params)
        assert requests.status_code == 200

    @pytest.mark.regression
    @parameterized.expand(RoadMap().get_list_of_endpoints_for_checking_with_get_method_negative_tests())
    def test_no_02_all_get_rows_negative(self, url: str, params: dict = None) -> None:
        """
        Test checks if endpoint doesn't work for API request.
        param url: url, which should be checked
        :param params: params for get method
        :return: None
        """
        requests = self.rest_method.get_request(url=url, params=params)
        assert requests.status_code == 400

    @pytest.mark.regression
    def test_no_03_test_get_post_put_delete_customer(self) -> None:
        """
        Test checks GET, PUT, POST, DELETE method for customer endpoint
        :return: None
        """
        url = RoadMap().customer_resource

        # Create new customer
        data = json.dumps(NEW_CUSTOMER_FOR_API_TESTS)
        request = self.rest_method.post_request(url=url, data=data, headers=self.headers)
        new_customer_id = json.loads(request.text)['id']
        assert request.status_code == 200

        # Create new customer - no data
        request = self.rest_method.post_request(url=url, headers=self.headers)
        assert (request.status_code == 500) or (request.status_code == 400)

        # Get customer
        customer_url = f'{url}{new_customer_id}'
        request = self.rest_method.get_request(url=customer_url)
        data = json.loads(request.text)
        assert request.status_code == 200
        assert data['id'] == new_customer_id

        # Update customer
        updated_customer = NEW_CUSTOMER_FOR_API_TESTS
        updated_customer['statusCode'] = 'ACTIVE'
        data = json.dumps(updated_customer)
        request = self.rest_method.put_request(url=customer_url, headers=self.headers, data=data)
        data = json.loads(request.text)
        assert request.status_code == 200
        assert data['status'] == 'active'

        # Update customer: no data
        request = self.rest_method.put_request(url=customer_url, headers=self.headers)
        assert (request.status_code == 500) or (request.status_code == 400)

        # Deleted customer
        request = self.rest_method.delete_request(url=customer_url, headers=self.headers)
        data = json.loads(request.text)
        sql_query = f"""
        select status
        from customer
        where id = '{new_customer_id}'
        """
        field_value = DatabaseMethods(user=DB_QA_USER, log=self.log).return_sql_query(sql_query=sql_query)

        assert request.status_code == 200
        assert data
        assert field_value[0][0] == 'DELETED'

    @pytest.mark.regression
    def test_no_04_test_get_calc_tolls(self):
        """
        Test takes from database first trip id, which has calculated toll, sends GET request and check if data
        is the same as data in database.
        :return: None
        """
        # Gets trip id, which has calc-tolls
        data_base_methods = DatabaseMethods(user=DB_QA_USER, log=self.log)
        sql_query = """
        select trip_id
        from calculated_toll;
         """
        trip_id = data_base_methods.return_sql_query(sql_query=sql_query)[0][0]

        # Gets toll_ids with GET method
        url = RoadMap().calc_toll_resource
        params = {'trip-id': trip_id}
        request = self.rest_method.get_request(url=url, params=params)
        toll_ids_api = [toll['id'] for toll in json.loads(request.text)]

        # Gets toll_ids from DB
        sql_query = f"""
        select id
        from calculated_toll
        where trip_id={trip_id};
        """
        toll_ids_from_db = data_base_methods.return_sql_query(sql_query=sql_query)
        toll_ids_from_db = [toll_id[0] for toll_id in toll_ids_from_db]

        assert request.status_code == 200
        assert toll_ids_api == toll_ids_from_db

    @pytest.mark.regression
    def test_no_05_test_create_get_put_delete_user(self):
        """
        Test checks GET, PUT, POST, DELETE method for user endpoint
        :return: None
        """

        url = RoadMap().users_resource

        # Create user (POST method)
        data = json.dumps(NEW_USER_FOR_API_TESTS)
        request = self.rest_method.post_request(url=url, data=data, headers=self.headers)
        assert request.status_code == 200
        customer_id = json.loads(request.text)['id']

        url = f'{url}{customer_id}'
        # Modify user (PUT method)
        NEW_USER_FOR_API_TESTS["statusCode"] = 'ACTIVE'
        request = self.rest_method.put_request(url=url, headers=self.headers, data=json.dumps(NEW_USER_FOR_API_TESTS))
        assert request.status_code == 200
        assert json.loads(request.text)['status'] == 'active'

        # Get user using user ID (GET method)
        request = self.rest_method.get_request(url=url)
        assert request.status_code == 200
        assert json.loads(request.text)['id'] == customer_id

        # Deletes user (DELETE method)
        request = self.rest_method.delete_request(url=url, headers=self.headers)
        assert request.status_code == 200
        assert json.loads(request.text)

        # Deletes deleted user (DELETE method)
        request = self.rest_method.delete_request(url=url, headers=self.headers)
        assert request.status_code == 200
        assert not json.loads(request.text)

    @pytest.mark.regression
    def test_no_06_get_user_with_customer_id_email(self):

        url = RoadMap().users_resource

        # Loads all customers and emails from DB
        sql_query = '''
        select customer_id, email
        from "user"
        '''
        data_base_methods = DatabaseMethods(user=DB_QA_USER, log=self.log)
        ids_emails = data_base_methods.return_sql_query(sql_query=sql_query)

        # Checking endpoint by with parameter customer_id
        customer_ids = [customer_id[0] for customer_id in ids_emails]
        for customer_id in set(customer_ids):
            params = {
                'customer-id': customer_id
            }
            request = self.rest_method.get_request(url=url, params=params)
            assert request.status_code == 200
            assert json.loads(request.text)[0]['customerId'] == customer_id

        # Checking endpoint by with parameter customer_id and email
        for customer_id, email in ids_emails:
            params = {
                'customer-id': customer_id,
                'email': email
            }
            request = self.rest_method.get_request(url=url, params=params)
            assert request.status_code == 200
            assert json.loads(request.text)[0]['customerId'] == customer_id
            assert json.loads(request.text)[0]['email'] == email

    @pytest.mark.regression
    def test_no_07_test_create_get_put_delete_vehicle(self):
        """
        Test checks GET, PUT, POST, DELETE method for vehicle endpoint
        :return: None
        """

        url = RoadMap().vehicles_resource

        # Create user (POST method)
        data = json.dumps(NEW_VEHICLE_FOR_API_TESTS)
        request = self.rest_method.post_request(url=url, data=data, headers=self.headers)
        assert request.status_code == 200
        vehicle_id = json.loads(request.text)['id']
        url = f'{url}{vehicle_id}'

        # Modify user (PUT method)
        new_vin = {"vin": '1N6ED0CE0MN7Z6280'}
        request = self.rest_method.put_request(url=url, headers=self.headers, data=json.dumps(new_vin))
        assert request.status_code == 200
        assert json.loads(request.text)['vin'] == new_vin["vin"]

        # Get user using user ID (GET method)
        request = self.rest_method.get_request(url=url)
        assert request.status_code == 200
        assert json.loads(request.text)['id'] == vehicle_id

        # Deletes user (DELETE method)
        request = self.rest_method.delete_request(url=url, headers=self.headers)
        assert request.status_code == 200
        assert json.loads(request.text)

        # Deletes user (DELETE method)
        request = self.rest_method.delete_request(url=url, headers=self.headers)
        assert request.status_code == 200
        assert not json.loads(request.text)

    @pytest.mark.regression
    def test_no_08_get_trip_by_customer_id_page_size_vehicle_id(self):
        """
        Test checks GET, PUT, POST, DELETE method for user endpoint
        :return: None
        """

        url = RoadMap().trips_resource
        page_size = 15
        vehicle_id = 384

        # Check if GET method works with default customer id
        params = {
            'customer-id': CUSTOMER_DEFAULT.user
        }
        request = self.rest_method.get_request(url=url, params=params)
        assert request.status_code == 200

        # Check if GET method works with default customer_id and page size. If fails on len, need to check data in DB.
        params = {
            'customer-id': CUSTOMER_DEFAULT.user,
            'page-size': page_size
        }
        request = self.rest_method.get_request(url=url, params=params)
        assert request.status_code == 200
        assert len(json.loads(request.text)['pageContent']) == page_size

        # Check if GET method works with default customer_id, page_size and vehicle. If fails on len,
        # need to check data in DB
        params = {
            'customer-id': CUSTOMER_DEFAULT.user,
            'page-size': page_size,
            'vehicle-id': vehicle_id,
        }
        request = self.rest_method.get_request(url=url, params=params)
        assert request.status_code == 200
        assert 0 < len(json.loads(request.text)['pageContent']) <= page_size
