"""
This file we use to send API request (it can be Rest API, GraphQK APIs, SOAP APIs ant others). It depends on
developers which API request form was choose, we just can write methods so send requests. Most popular methods are
GET, PUT, DELETE, POST. If we need more (need to read requirement for tests), we create extend our methods.

Manually we can use such tolls as Postman, swagger and others.
"""


import logging
from typing import Optional, Union

import requests
from requests import Response


class RestMethods:
    """
    Methods for API tests
    """

    def __init__(self, log: logging = None):
        self.log = log

    def post_request(self, url, headers: Optional = None, data: Optional = None) -> Response:
        """
        Sends POST request to URL.
        :param url: url of request
        :param headers: request headers
        :param data: data of request
        :return: Response object
        """
        self.log.info(f"Sending url POST request for {url}")
        response = requests.post(url, data=data, headers=headers)
        self.log.info(f'Status is {response.status_code}')
        return response

    def get_request(self, url, params: dict = None) -> Response:
        """
        Sends GET request
        :param url: url of request
        :param params: data of request
        :return: response of request
        """
        self.log.info(f"Sending url GET request for {url}")
        response = requests.get(url, params=params)
        self.log.info(f'Status is {response.status_code}')
        return response

    def delete_request(self, url, data: Union[dict, str] = None, headers: Optional = None, ) -> Response:
        """
        Sends GET request
        :param url: url of request
        :param params: data of request
        :return: response of request
        """
        self.log.info(f"Sending url GET request for {url}")
        response = requests.delete(url, data=data, headers=headers)
        self.log.info(f'Status is {response.status_code}')
        return response

    def put_request(self, url, data: Union[dict, str] = None, headers: Optional = None, ) -> Response:
        """
        Sends PUT request
        :param url: url of request
        :param params: data of request
        :return: response of request
        """
        self.log.info(f"Sending url GET request for {url}")
        response = requests.put(url, data=data, headers=headers)
        self.log.info(f'Status is {response.status_code}')
        return response
