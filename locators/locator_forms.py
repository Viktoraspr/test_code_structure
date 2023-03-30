"""
I suggest to see at locator as object. Then it's easy create loggers, to add additional info, etc.

CallSimpleLocatorForm - I use this class to create locator, when locators depend on for sample column name.
"""

from dataclasses import dataclass


@dataclass
class SimpleLocatorForm:
    """
    Name and locator
    """
    name: str
    locator: tuple
    url: str = ''

    def __str__(self):
        return f'Fields {self.name}, locator: {self.locator}'


class CallSimpleLocatorForm:
    """
    We need this call to create locator for locators, which depends on field name
    :param name: name, which we use printing info
    :param locator: locator in portal.
    """

    def __init__(self, name: str, locator: tuple):
        self.name = name
        self.locator = locator

    def __call__(self, field_value: str) -> SimpleLocatorForm:
        locator = (self.locator[0], self.locator[1].format(value=self.name))
        field = SimpleLocatorForm(
            name=self.name,
            locator=locator,
        )
        return field
