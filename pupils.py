"""
File: L11 Teach: Team Activity
Author: Gab Yanqui
Date: 03/23/2023
Purpose: Reinforce in your mind the concept that a function can be passed as an argument into another function. 
"""
"""
The CSV file named pupils.csv contains data about 100 students. Unfortunately, the data is not sorted. As a team,
write a program that reads the contents of pupils.csv into a compound list, sorts the list by birthday from oldest
to youngest, and then prints the list with the data about each student on a separate line.
"""

import csv

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    try:
        students_list = read_compound_list("pupils.csv")

        give_name_extractor = lambda student: student[GIVEN_NAME_INDEX]
        students_list = sorted(students_list, key=give_name_extractor)
        print_list(students_list)


        sorted_list_3 = sort_by_birth_month_day(students_list)
        print("Ordered by Birth Month and Day")
        print_list(sorted_list_3)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

def sort_by_birth_month_day(students_list):
    """Sort a list of students by their birth month and day.
    In other words sort the list by their birthdate but ignore
    the year of their birthdate.

    Parameter
        students_list: a list that contains small lists.
            Each small list contains the given name,
            surname, and birthdate of one student.
    Return: a new list of students that is sorted by birth
        month and day.
    """
    # Define a nested function that extracts
    # a student's birthdate without the year.
    def extract_month_and_day(student):
        birthdate_string = student[BIRTHDATE_INDEX]
        # Month and date started in index 5 for brithdate_index
        month_and_day = birthdate_string[5:]
        return month_and_day

    # Call the sorted function to sort the list
    # of students by their birth month and day.
    sorted_list = sorted(students_list, key=extract_month_and_day)

    # Return the sorted list.
    return sorted_list

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):

    for items in list:
        print(items)
    print() # Blank line

if __name__ == "__main__":
    main()


