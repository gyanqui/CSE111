"""
File: L05 Teach: Team Activity
Author: Gab Yanqui
Date: 01/31/2023
Purpose: Test fuction using pytest and assert statements.
"""
"""Verify that the extract_city, extract_state and
extract_zipcode functions work correctly.
"""

from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the extract_city 2 times and use an assert
    # statement to verify that the strings returned is
    # correct each time
    assert extract_city("507 S Hoff Ave, El Reno, OK 73036") == "El Reno"
    assert extract_city("1841 Diamond Lake Trl, Justin, TX 76247") == "Justin"  

def test_extract_state():
    """Verify that the extract_city function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the extract_state 2 times and use an assert
    # statement to verify that the strings returned is
    # correct each time
    assert extract_state("507 S Hoff Ave, El Reno, OK 73036") == "OK"
    assert extract_state("1841 Diamond Lake Trl, Justin, TX 76247") == "TX"  

def test_extract_zipcode():
    """Verify that the extract_city function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the extract_zipcode 2 times and use an assert
    # statement to verify that the strings returned is
    # correct each time
    assert extract_zipcode("507 S Hoff Ave, El Reno, Ok 73036") == "73036"
    assert extract_zipcode("1841 Diamond Lake Trl, Justin, TX 76247") == "76247"  

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
