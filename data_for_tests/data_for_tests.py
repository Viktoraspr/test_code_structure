"""
Tests' data.
"""
from properties.config import TestData
from data_for_tests.data_dataclass_forms import Customer, MessageData, Agency, TRA, \
    TDA, VehicleClass, TollRat
CUSTOMER_NEW = Customer(
    name='Test',
    email='test@test.com',
    address='Lvovo st. 25-146, Vilnius',
    database='MeWar',
    integration='No',
    user='fbadfgbdfgb',
    password='saggsags'
)

CUSTOMER_EDITED = Customer(
    name='Test Test',
    email='test@test.com',
    address='Lvovo st. 25-122, Vilnius',
    database='Welink',
    integration='No',
    user='frghwrhgewr',
    password='reghwerhg'
)

MESSAGE_CORRECT = MessageData(
    name='Test',
    organization='TestTest',
    email='test@test.com',
    phone='+37061234567',
    message='Test',
)

MESSAGE_INCORRECT = MessageData(
    name='Test',
    phone='Test',
)

CUSTOMER_DEFAULT = Customer(
    name='mabgib',
    email='sfgweg@mail.lt',
    address='Utah',
    user='4e2dcbb0-f169-11ec-aab4-3bfb0d27e839',
    status='ACTIVE',
    database='bewar',
    password='adsag==',
    integration='No',
)

NEW_CUSTOMER_FOR_API_TESTS = {
    "adminEmail": "asg@tateas.lt",
    "companyName": "sadg asgerg",
    "companyAddress": "Vilfvdvnius",
    "companyLogo": "true",
    "statusCode": "INVITE_SENT",
    "geotabIntegration": "false",
    "geotabDatabase": "None",
    "geotabServiceUser": "testas@aafdaf",
    "geotabServicePassword": "sdgsag",
    "phoneNumber": "19199"
}

NEW_USER_FOR_API_TESTS = {
    "name": "New user",
    "email": "new_user@email.com",
    "customerId": "49494949",
    "statusCode": "INVITE_SENT",
    "roleCode": "ADMINISTRATOR",
    "sourceType": "DIRECT"
}

NEW_VEHICLE_FOR_API_TESTS = {
    "name": "Test vehicle",
    "type": "Auto",
    "vin": "1N6ED0CE0MN706280",
    "plateState": "",
    "plateNumber": "Unknown",
    "weight": 16000,
    "height": 2,
    "axles": 2,
    "wheels": 4,
    "tires": 0,
    "vehicleClass": "CLASS_2A",
    "deviceId": "b5",
    "customerId": CUSTOMER_DEFAULT.user,
    "tagType": "TOLLTAG",
    "tagTransponder": "DFW.89072636",
    "issuingAgencyId": 21,
    "currentDriver": "Big Tester",
}

AGENCY_NEW = Agency(
    state='Alabama',
    agency_name='Test'
)

TRA_NEW = TRA(
    description='TRA',
    latitude='37.82471632662249',
    longitude='-122.31379629570995'
)

TRA_EDITED = TRA(
    description='TRA-Agency',
    latitude='38.02462992964815',
    longitude='-121.75168561328842'
)

TDA_NEW = TDA(
    wide_area='0.0309',
    nearby_area='20',
    latitude='37.82471632662249',
    longitude='-122.31379629570995',
    tda_type='BARRIER_PLAZA'
)

TDA_EDITED = TDA(
    wide_area='0.0309',
    nearby_area='30',
    latitude='38.52171132262251',
    longitude='-121.18775625570699',
    tda_type='DISTANCE_PLAZA'
)

VEHICLE_CLASS_NEW = VehicleClass(
    name='TT.1',
    vehicle_type='AUTO, COMMERCIAL, BUS',
    weight='From 0 to 150000',
    height='From 0 to 150',
    vehicle_axles='From 2 to 14',
    vehicle_tires='From 4 to 28'
)

VEHICLE_CLASS_EDITED = VehicleClass(
    name='TT.2',
    vehicle_type='AUTO, COMMERCIAL',
    weight='From 14000 to 14000',
    height='From 25 to 25',
    vehicle_axles='From 5',
    vehicle_tires='From 4'
)

TOLL_RATE_NEW = TollRate(
    rate_class='[1]',
    toll_amount='100',
    payment_type='[1]',
    start_date=TestData.today_date,
    end_date=TestData.new_date
)

TOLL_RATE_EDITED = TollRate(
    rate_class='[1]',
    toll_amount='700',
    payment_type='[11]',
    start_date=TestData.today_date,
    end_date=TestData.new_date
)
