import unittest

from domeniu.validators import *
from domeniu.entities import *


def test_valid_date():
    date = '14/02'
    error_list = valid_date(date)
    assert len(error_list) == 0

    date1 = '-1/cc'
    error_list = valid_date(date1)
    assert len(error_list) == 2


def test_valid_time():
    time = "14:22"
    error_list = valid_time(time)
    assert len(error_list) == 0

    error_list = valid_time("cc:21")
    assert len(error_list) == 1


def validators_tests():
    test_valid_date()
    test_valid_time()

