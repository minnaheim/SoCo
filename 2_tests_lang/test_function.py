# import unittest
from 2_tests_lang/functions.py import functions


def test_add_good():
    assert functions.add_(3, 4) == 7


def test_add_wrong():
    assert functions.add_(4, 4) == 5
