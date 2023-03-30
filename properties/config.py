"""
This file contains basic data for tests
"""

import os
from datetime import datetime

from dateutil.relativedelta import relativedelta

TIMEOUT = 15


class TestData:
    """
    Global variables data
    """
    BROWSER = os.getenv('BROWSER', 'chrome')
    BROWSER_WINDOW_SIZE = os.getenv('BROWSER_WINDOW_SIZE', '1920,1080')
    BROWSER_MODE = os.getenv('BROWSER_MODE', 'with head')
    SCREENSHOT = os.getenv('SCREENSHOT', 'True')
    reports_path = os.getcwd() + "/reports"
    part_url = "http://here_we_add_our_urls_"
    WEB_PORTAL_URL = 'http://here_we_add_our_urls_'
    WEB_PORTAL_TOLL_LOGIC_URL = 'http://here_we_add_our_web_portal_url'
    today_date = datetime.today().strftime("%Y-%m-%d") + " 00:00:00"
    new_date = (datetime.today() + relativedelta(years=1)).strftime("%Y-%m-%d") + " 00:00:00"
    toll_guru_aws_url = "http://here_we_add_our_urls"
    toll_guru_aws_headers = {"Content-Type": "application/json",
                             "Accept": "*/*",
                             "Accept-Encoding": "gzip, deflate, br",
                             "Connection": "keep-alive",
                             "x-api-key": "xxxxxxx"}
    trip_id_first = "3352"
    trip_id_second = "11518"
    toll_guru_aws_timestamp = datetime.today() - relativedelta(hours=3)
    toll_guru_aws_timestamp = toll_guru_aws_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    logging_dir = "C:/commerce-logic_repo/cl-qa/logs/"
    toll_calculations_url = "http://here_we_add_our_urls_for_test"
