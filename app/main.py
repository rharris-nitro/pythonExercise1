"""
This module serves as the entry point for the Python application. It initializes the Data class
and uses it to print an array of integers to the console.
"""

import argparse

from app.data import Data


def read_file(file_path):
    """
    Reads a file and returns an array of integers.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [int(x) for x in file.read().split()]


def main(file_path):
    """
    Main function for creating a Data instance and printing the array.

    This function demonstrates the basic usage of the Data class by creating an instance,
    initializing it with the contents of a file, and then printing this array.
    """
    integer_array = read_file(file_path)
    data = Data(integer_array)
    data.print_array()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file containing integers.")
    parser.add_argument(
        "--file_path",
        default="app/input/integers.txt",
        type=str,
        help="Path to the file containing integers",
    )
    args = parser.parse_args()
    main(args.file_path)
