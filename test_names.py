"""
File: L05 Teach: Team Activity
Author: Gab Yanqui
Date: 01/31/2023
Purpose: Test fuction using pytest and assert statements.
"""
"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the make_full_name 4 times and use an assert
    # statement to verify that the strings returned by the 
    # make_full_name is the correct each time
    assert make_full_name("Juan", "Munoz") == "Munoz; Juan"
    assert make_full_name("Job", "Ugarte") == "Ugarte; Job"
    assert make_full_name("Luciana", "Barrera") == "Barrera; Luciana"
    assert make_full_name("Arlet", "Uriarte") == "Uriarte; Arlet"
    assert make_full_name("Lee-Ho", "W") == "W; Lee-Ho"

def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the extract_family_name 4 times and use an assert
    # statement to verify that the strings returned by the 
    # extract_given_name is the correct each time
    assert extract_family_name("Chavez; Luis") == "Chavez"
    assert extract_family_name("Perez; Teresa") == "Perez"
    assert extract_family_name("Amado; Carla") == "Amado"
    assert extract_family_name("Ramos; Jose") == "Ramos"
    
def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    
    Parameters: none
    Return: nothing
    """
    # Call the extract_given_name 4 times and use an assert
    # statement to verify that the strings returned by the 
    # extract_given_name is the correct each time
    assert extract_given_name("Alvarez; Richard") == "Richard"
    assert extract_given_name("Wang; Lee-J") == "Lee-J"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
