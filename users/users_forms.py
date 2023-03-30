"""
This file contains users classes: DB users, portal users.
"""

from dataclasses import dataclass


@dataclass
class DataBaseUser:
    """This class is for creating DB user"""
    username: str = None
    password: str = None
    host: str = None
    port: str = None
    database: str = None


@dataclass
class WebUser:
    """This class is for creating WEB user"""
    email: str = None
    password: str = None
