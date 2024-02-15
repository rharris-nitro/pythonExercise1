"""
Module test_main: This module contains test cases for the Main class in app.main.
"""

from app.main import Main


def test_correct_array():
    """
    Test case to ensure the initialized array is correct.
    """
    main_instance = Main()
    assert main_instance.integer_array == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_incorrect_array():
    """
    Test case to ensure the initialized array is not incorrect.
    """
    main_instance = Main()
    assert main_instance.integer_array != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
