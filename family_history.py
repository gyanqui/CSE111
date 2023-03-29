"""
File: L08 Teach: Team Activity
Author: Gab Yanqui
Date: 02/21/2023
Purpose: Practice with dictionaries 
"""
"""Write a Python program that stores data about individuals in one dictionary
and stores data about marriages in a different dictionary. Your program must
combine the data in the two dictionaries and print the combined data so that
it is understandable to a user.
"""
# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3
NUM_MARRIAGES_INDEX = 4


# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2

def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    # Print a blank line.
    print()

    count_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print('Ages at Death')
    print()# Blank line

    for key, value in people_dict.items(): 
        name = value[NAME_INDEX]
        birth = value[BIRTH_YEAR_INDEX]
        death = value[DEATH_YEAR_INDEX]

        age_death = death - birth
        print(name, age_death)

def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print('Genders')
    print()# Blank line

    male = 0
    female = 0

    for key, value in people_dict.items():
        gender = value[GENDER_INDEX]
        if gender.upper() == "M":
            male += 1
        else:
            female += 1

    print(f'Number of males: {male}')
    print(f'Number of females: {female}')

def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print('Marriages')
    print()# Blank line

    for key, value in marriages_dict.items():
        husband = value[HUSBAND_KEY_INDEX]
        wedding = value[WEDDING_YEAR_INDEX]
        wife = value[WIFE_KEY_INDEX]

        husband_data = people_dict[husband]
        husband_name = husband_data[NAME_INDEX]
        husband_birth = husband_data[BIRTH_YEAR_INDEX]

        husband_age = wedding - husband_birth

        wife_data = people_dict[wife]
        wife_name = wife_data[NAME_INDEX]
        wife_birth = wife_data[BIRTH_YEAR_INDEX]

        wife_age = wedding - wife_birth

        print(f'{husband_name} {husband_age} > {wedding} < {wife_name} {wife_age}')

def count_marriages(marriages_dict, people_dict):

    print('Who marriages the most')
    print() # Blank line

    for key, value in people_dict.items():
        value.append(0)

    for key, value in marriages_dict.items():

        husband_id = value[HUSBAND_KEY_INDEX]
        wife_id = value[WIFE_KEY_INDEX]

        husband_data = people_dict[husband_id]
        husband_data[NUM_MARRIAGES_INDEX] += 1

        wife_data = people_dict[wife_id]
        wife_data[NUM_MARRIAGES_INDEX] += 1
        
    for key, value in people_dict.items(): 
        name = value[NAME_INDEX]
        num_marriages = value[NUM_MARRIAGES_INDEX]

        print(name, num_marriages)

    max_marriages = -1
    most_married_person = None

    for key, value in people_dict.items():
        if value[4] > max_marriages:
            max_marriages = value[4]
            most_married_person = value[0]    

    print() # Blank line
    print("The person who has been married the most is", most_married_person, "with", max_marriages, "marriages.")

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()