"""
File: L07 & L08 Prove: Assignment
Author: Gab Yanqui
Date: 02/25/2023
Purpose: Write a Python program that uses a dictionary and lists.
"""
"""
Write and test a molar mass calculator named chemistry.py. During
this milestone, you will complete part of the calculator by writing
a function named make_periodic_table and the main function. The
make_periodic_table function must create and return a compound
list that contains data for all 94 naturally occuring elements.
"""
"""
Write and test the remaining parts of the molar mass calculator that
you started writing in the previous lesson’s prove milestone. When
you are finished with this prove assignment, your chemistry.py program
must contain at least three functions named as follows:

main
make_periodic_table
compute_molar_mass
"""

from formula import parse_formula

SYMBOL = 0
NAME = 1
ATOMIC_MASS = 2

def main():
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table = make_periodic_table()

    # Get a chemical formula for a molecule from the user.
    molecule = input('Enter the molecular formula of the sample: ')
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    compound_list = parse_formula(molecule, periodic_table)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(compound_list, periodic_table)

    # Get the mass of a chemical sample in grams from the user.
    mass = float(input('Enter the mass in grams of the sample: '))

    # Compute the number of moles in the sample.
    moles = mass / molar_mass

    # Print the molar mass.
    print('Molar mass:', molar_mass, 'g/mol')

    # Print the number of moles.
    print(f'Number of moles: {moles:.5f}')

    total_protons = sum_protons(compound_list, periodic_table)
    print("Compound: ", compound_list)
    print("Total protons: ", total_protons)

def make_periodic_table():
    """Create and return the periodic table list
    Return: the periodic table list.
    """

    periodic_table_list = {
    # symbol: [name, atomic_mass, atomic_number]
    "Ac": ["Actinium", 227, 89],
    "Ag": ["Silver", 107.8682, 47],
    "Al": ["Aluminum", 26.9815386, 13],
    "Ar": ["Argon", 39.948, 18],
    "As": ["Arsenic", 74.9216, 33],
    "At": ["Astatine", 210, 85],
    "Au": ["Gold", 196.966569, 79],
    "B": ["Boron", 10.811, 5],
    "Ba": ["Barium", 137.327, 56],
    "Be": ["Beryllium", 9.012182, 4],
    "Bi": ["Bismuth", 208.9804, 83],
    "Br": ["Bromine", 79.904, 35],
    "C": ["Carbon", 12.0107, 6],
    "Ca": ["Calcium", 40.078, 20],
    "Cd": ["Cadmium", 112.411, 48],
    "Ce": ["Cerium", 140.116, 58],
    "Cl": ["Chlorine", 35.453, 17],
    "Co": ["Cobalt", 58.933195, 27],
    "Cr": ["Chromium", 51.9961, 24],
    "Cs": ["Cesium", 132.9054519, 55],
    "Cu": ["Copper", 63.546, 29],
    "Dy": ["Dysprosium", 162.5, 66],
    "Er": ["Erbium", 167.259, 68],
    "Eu": ["Europium", 151.964, 63],
    "F": ["Fluorine", 18.9984032, 9],
    "Fe": ["Iron", 55.845, 26],
    "Fr": ["Francium", 223, 87],
    "Ga": ["Gallium", 69.723, 31],
    "Gd": ["Gadolinium", 157.25, 64],
    "Ge": ["Germanium", 72.64, 32],
    "H": ["Hydrogen", 1.00794, 1],
    "He": ["Helium", 4.002602, 2],
    "Hf": ["Hafnium", 178.49, 72],
    "Hg": ["Mercury", 200.59, 80],
    "Ho": ["Holmium", 164.93032, 67],
    "I": ["Iodine", 126.90447, 53],
    "In": ["Indium", 114.818, 49],
    "Ir": ["Iridium", 192.217, 77],
    "K": ["Potassium", 39.0983, 19],
    "Kr": ["Krypton", 83.798, 36],
    "La": ["Lanthanum", 138.90547, 57],
    "Li": ["Lithium", 6.941, 3],
    "Lu": ["Lutetium", 174.9668, 71],
    "Mg": ["Magnesium", 24.305, 12],
    "Mn": ["Manganese", 54.938045, 25],
    "Mo": ["Molybdenum", 95.96, 42],
    "N": ["Nitrogen", 14.0067, 7],
    "Na": ["Sodium", 22.98976928, 11],
    "Nb": ["Niobium", 92.90638, 41],
    "Nd": ["Neodymium", 144.242, 60],
    "Ne": ["Neon", 20.1797, 10],
    "Ni": ["Nickel", 58.6934, 28],
    "Np": ["Neptunium", 237, 93],
    "O": ["Oxygen", 15.9994, 8],
    "Os": ["Osmium", 190.23, 76],
    "P": ["Phosphorus", 30.973762, 15],
    "Pa": ["Protactinium", 231.03588, 91],
    "Pb": ["Lead", 207.2, 82],
    "Pd": ["Palladium", 106.42, 46],
    "Pm": ["Promethium", 145, 61],
    "Po": ["Polonium", 209, 84],
    "Pr": ["Praseodymium", 140.90765, 59],
    "Pt": ["Platinum", 195.084, 78],
    "Pu": ["Plutonium", 244, 94],
    "Ra": ["Radium", 226, 88],
    "Rb": ["Rubidium", 85.4678, 37],
    "Re": ["Rhenium", 186.207, 75],
    "Rh": ["Rhodium", 102.9055, 45],
    "Rn": ["Radon", 222, 86],
    "Ru": ["Ruthenium", 101.07, 44],
    "S": ["Sulfur", 32.065, 16],
    "Sb": ["Antimony", 121.76, 51],
    "Sc": ["Scandium", 44.955912, 21],
    "Se": ["Selenium", 78.96, 34],
    "Si": ["Silicon", 28.0855, 14],
    "Sm": ["Samarium", 150.36, 62],
    "Sn": ["Tin", 118.71, 50],
    "Sr": ["Strontium", 87.62, 38],
    "Ta": ["Tantalum", 180.94788, 73],
    "Tb": ["Terbium", 158.92535, 65],
    "Tc": ["Technetium", 98, 43],
    "Te": ["Tellurium", 127.6, 52],
    "Th": ["Thorium", 232.03806, 90],
    "Ti": ["Titanium", 47.867, 22],
    "Tl": ["Thallium", 204.3833, 81],
    "Tm": ["Thulium", 168.93421, 69],
    "U": ["Uranium", 238.02891, 92],
    "V": ["Vanadium", 50.9415, 23],
    "W": ["Tungsten", 183.84, 74],
    "Xe": ["Xenon", 131.293, 54],
    "Y": ["Yttrium", 88.90585, 39],
    "Yb": ["Ytterbium", 173.054, 70],
    "Zn": ["Zinc", 65.38, 30],
    "Zr": ["Zirconium", 91.224, 40]
    }

    return periodic_table_list

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    parse_formula

    total_molar_mass = 0.0 

    # Do the following for each inner list in the
    # compound symbol_quantity_list:
    for i in symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        symbol = i[SYMBOL_INDEX]
        quantity = i[QUANTITY_INDEX]
        # Get the atomic mass for the symbol from the dictionary.
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        # Multiply the atomic mass by the quantity.
        product = atomic_mass * quantity
        # Add the product into the total molar mass.
        total_molar_mass += product

    # Return the total molar mass.
    return total_molar_mass

ATOMIC_NUMBER = 2

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """
    total_protons = 0
    for symbol, quantity in symbol_quantity_list:
        element_dict = periodic_table_dict[symbol]
        atomic_number = element_dict[ATOMIC_NUMBER]
        total_protons += atomic_number * quantity
        element_dict[ATOMIC_NUMBER] = atomic_number
    return total_protons

# Call main to start this program.
if __name__ == "__main__":
    main()