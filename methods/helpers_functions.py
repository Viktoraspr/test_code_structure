"""
All functions to help manipulate data.


Such types of files we use to create some functions to manipulate with data, etc.
"""


def get_list_of_values_from_dictionary(list_of_matched_areas: list[dict], key: str) -> list[str]:
    """
    Get all id's values in list
    :param locator: barrier or segment id, tollRateId, CalculatedAmount
    :param list_of_matched_areas: list of barriers or segments or tollDto
    :return: id of trips
    """
    ids = []
    for value in list_of_matched_areas:
        ids.append(value[key])
    return ids
