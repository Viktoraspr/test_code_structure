"""
This file contains classes for creating login/users object.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    """
    Class for creating customer
    """
    name: str = None
    email: str = None
    address: str = None
    database: str = None
    integration: str = None
    user: str = None
    password: str = None
    status: str = None


@dataclass
class MessageData:
    """
    Class for messages
    """
    name: str = ''
    organization: str = ''
    email: str = ''
    phone: str = ''
    message: str = ''


@dataclass
class Agency:
    """
    Class for creating agencies
    """
    state: str = None
    agency_name: str = None


@dataclass
class TRA:
    """
    Class for creating TRA
    """
    description: str = None
    latitude: str = None
    longitude: str = None


@dataclass
class TDA:
    """
    Class for creating TDA
    """
    wide_area: str = None
    nearby_area: str = None
    latitude: str = None
    longitude: str = None
    tda_type: str = None


@dataclass
class VehicleClass:
    """
    Class for creating vehicle classes
    """
    name: str = None
    vehicle_type: str = None
    weight: str = None
    height: str = None
    vehicle_axles: str = None
    vehicle_tires: str = None


@dataclass
class TollRate:
    """
    Class for creating toll rates
    """
    rate_class: str = None
    toll_amount: str = None
    payment_type: str = None
    start_date: datetime = None
    end_date: datetime = None
