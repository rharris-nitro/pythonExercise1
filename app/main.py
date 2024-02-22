"""
Module main: This module contains the main function that initializes an array
of integers and prints it.
"""


class Data:
    """
    Main class for handling integer arrays.
    """

    def __init__(self):
        """
        Initializes an array of integers with predefined values.
        """
        self.integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def print_array(self):
        """
        Prints the initialized array to the screen.
        """
        print(self.integer_array)

    def get_array(self):
        """
        Returns the initialized array.
        """
        return self.integer_array


def main():
    """
    Main function for creating Main instance and printing the array.
    """
    data = Data()
    data.print_array()


if __name__ == "__main__":
    main()
