import re
import os


def validate_date(date):
    """Method to validate date
    :param date : Type String : date captured from webserver log
    :return: True if a valid date
             False if not a valid date
    """
    pattern = re.compile(
        r'^(([0-9])|([0-2][0-9])|([3][0-1]))\/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\/\d{4}$')
    m = pattern.search(date)
    if m:
        return True
    return False


def is_valid_path(file):
    """Method to validate file path
    :param file : Type String : path to file
    :return: True if a valid path to file
             False if not a valid path to file
    """
    if os.path.exists(file):
        return True
    return False


def is_valid_file(file):
    """Method to validate file
    :param file : Type String : path to file
    :return: True if file is valid
             False if file is not valid
    """
    if os.path.isfile(file):
        return True
    return False
