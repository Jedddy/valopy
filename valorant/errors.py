"""Errors received from the API"""


class ValError(Exception):
    """Val"""


class NotFound(ValError):
    """Raised when something isn't found"""
