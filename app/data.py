"""
This module defines the Data class, which is responsible for initializing and managing
an array of integers. It provides methods to print the array and potentially other
operations related to the array.
"""


class Data:
    """
    A class representing a data structure that holds an array of integers.

    Attributes:
        array (list): An array of integers.
    """

    def __init__(self):
        """
        Initializes the Data object with a predefined array of integers.
        """
        self.__integer_array = [1, 2, 3, 4, 5]

    def print_array(self):
        """
        Prints the array of integers to the console.
        """
        print(self.__integer_array)

    def get_array(self):
        """
        Returns the initialized array.
        """
        return self.__integer_array
