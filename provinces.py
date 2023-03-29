"""
File: L08 Prepare Checkpoint
Author: Gab Yanqui
Date: 02/28/2023
Purpose: Practice writing code that reads from a text file into a list. 
"""
"""
Write a Python program named provinces.py that reads the contents
of provinces.txt into a list and then modifies the list.
"""

import csv

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("provinces.txt")


    print(text_list)

    del text_list[0]

    text_list.pop()

    print()

    print(text_list)

    for i in range(len(text_list)):

        if text_list[i] == 'AB':

            text_list[i] = 'Alberta'

    print()

    print(text_list)

    print()

    count_alberta = text_list.count('Alberta')
    print(count_alberta)

    print()


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open('provinces.txt', "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()