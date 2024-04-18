"""
This module serves as the entry point for the Python application. It initializes the Data class
and uses it to print an array of integers to the console.
"""

from app.data import Data


def main():
    """
    Main function for creating a Data instance and printing the array.

    This function demonstrates the basic usage of the Data class by creating an instance,
    initializing it with a predefined array of integers, and then printing this array.
    """
    data = Data()
    data.print_array()


if __name__ == "__main__":
    main()
