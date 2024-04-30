"""
Module test_main: This module contains test cases for the Main class in app.main.
"""

from app.data import Data


def test_get_array():
    """
    Test case to ensure the initialized array is correct.
    """
    data = Data()
    assert data.get_array() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_get_wrong_array():
    """
    Test case to ensure the initialized array is not incorrect.
    """
    data = Data()
    assert data.get_array() != [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]


def test_print_array(capsys):
    """
    Test case to ensure the print_array method prints the correct array.
    """
    data = Data()
    data.print_array()
    captured = capsys.readouterr()
    assert captured.out == "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
