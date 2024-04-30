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

    def __init__(self, integer_array=None):
        """
        Initializes the Data object with a predefined array of integers
        or an empty array if none is provided.
        """
        if integer_array is None:
            self.__integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        else:
            self.__integer_array = integer_array

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
