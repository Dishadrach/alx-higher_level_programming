#!/usr/bin/python3
"""
Class BaseGeometry based in the last task
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """'area()' method"""
        raise Exception("area() is not implemented")

    """'integer_validator()'method"""
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
