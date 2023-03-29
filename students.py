

import csv

def main():

    I_NUMBER = 0
    NAME_INDEX = 1

    students_dict = read_dictionary("students.csv", I_NUMBER)

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
            value = students_dict[id]
            name = value[NAME_INDEX]
        # Print the student's name.
            print(name)

    else:
        print("No such student")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}


    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]
            # Store the data from the current
            # row into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()