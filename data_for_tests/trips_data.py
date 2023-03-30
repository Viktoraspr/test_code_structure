"""
In this file we keep data, which we should get when we use requests.get() method.
"""

TRIP136515 = {
    'id': '136515',
    'segments': [],
    'barriers': ['4a7cfb14-a135-11ec-b81b-437a1679f4c5', '3d0e56c2-a143-11ec-9dae-b31da645885c',
                 '83a45926-a63c-11ec-bf72-cfad6a451250', 'ffae860e-a637-11ec-b309-9316fe1ece12',
                 'f85faa94-a197-11ec-8e5a-131ea95bba0a'],
    "calculatedTripToll": {
        "tollDtoList": [
            {"tollRateId": 214142, "calculatedAmount": 232}, {"tollRateId": 214062, "calculatedAmount": 444},
            {"tollRateId": 214252, "calculatedAmount": 596}, {"tollRateId": 214212, "calculatedAmount": 552},
            {"tollRateId": 214652, "calculatedAmount": 800}],
        'totalAmount': 2624
    }
}

TRIP130119 = {
    'id': '130119',
    'segments': [],
    'barriers': ['f3212ddc-a115-11ec-93ad-db51822924c7', '3d0e56c2-a143-11ec-9dae-b31da645885c'],
    "calculatedTripToll": {
        "tollDtoList": [
            {"tollRateId": 214034, "calculatedAmount": 625}, {"tollRateId": 214064, "calculatedAmount": 555}],
        'totalAmount': 1180
    }
}

TRIP130082 = {
    'id': '130082',
    'segments': [],
    'barriers': ['ee26e350-a39d-11ec-9376-23f8f64703db'],
    "calculatedTripToll": {
        "tollDtoList": [
            {"tollRateId": 214572, "calculatedAmount": 492}],
        'totalAmount': 492
    }
}
