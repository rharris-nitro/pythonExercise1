"""
Data class
"""


class Data:
    """
    Main class for handling integer arrays.
    """

    def __init__(self):
        """
        Initializes an array of integers with predefined values.
        """
        self.__integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def print_array(self):
        """
        Prints the initialized array to the screen.
        """
        print(self.__integer_array)

    def get_array(self):
        """
        Returns the initialized array.
        """
        return self.__integer_array
