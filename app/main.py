"""
Module main: This module contains the main function that initializes an array
of integers and prints it.
"""


class Main:
    """
    Main class for handling integer arrays.
    """

    def __init__(self):
        """
        Initializes an array of integers with predefined values.
        """
        self.integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # self.integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def print_array_to_the_screen(self):
        """
        Prints the initialized array to the screen.
        """
        # printing array
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
    main_instance = Main()
    main_instance.print_array_to_the_screen()


if __name__ == "__main__":
    main()
