"""
File: L06 Prove: Assignment
Author: Gab Yanqui
Date: 02/11/2023
Purpose: Test fuction using pytest and assert statements.
"""
"""Verify that the get_determiner, get_noun, get_verb,
get_preposition, get_prepositional_phrase functions work correctly.
"""
from sentences import get_determiner, \
    get_noun, get_verb, get_preposition, \
    get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    """Verify that the get_determiner function works correctly.

    Parameters: none
    Return: nothing
    """
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    """Verify that the get_noun function works correctly.

    Parameters: none
    Return: nothing
    """
    # 1. Test the single noun.
    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)
        # Verify that the word returned from get_noun
        # is one of the words in the single_noun list.
        assert word in single_noun

    # 2. Test the plural nouns.
    plural_nouns = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)
        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    """Verify that the get_verb function works correctly.

    Parameters: none
    Return: nothing
    """
    # Define the different verb lists
    past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    single_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    plural_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Test the past tense with quantity = 1
    for _ in range(11):
        verb = get_verb(1, "past")
        assert verb in past

    # Test the single present tense with quantity = 1
    for _ in range(11):
        verb = get_verb(1, "present")
        assert verb in single_present

    # Test the plural present tense with quantity = 2
    for _ in range(11):
        verb = get_verb(2, "present")
        assert verb in plural_present

    # Test the future tense with quantity = 1
    for _ in range(11):
        verb = get_verb(1, "future")
        assert verb in future

def test_get_preposition():
    """Verify that the get_preposition function works correctly.

    Parameters: none
    Return: nothing
    """
    # Define the preposition lists
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of","off", "on", "onto", "out",
    "over", "past", "to", "under", "with", "without"]

    # Test the preposition
    for _ in range(31):
        word = get_preposition()
        assert word in preposition

def test_get_prepositional_phrase():
    """Verify that the get_prepositional_phrase function works correctly.

    Parameters: none
    Return: nothing
    """
    # Define the determiners, nouns, prepositions lists
    determiners = ["a", "one", "the", "some", "many", "the"]
    nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of","off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    # Call the get_noun function which should return a prepositional phrase.
    prepositional_phrase = get_prepositional_phrase(1)
    # Use the split function to split the prepositional phrase
    words = prepositional_phrase.split()
    assert len(words) == 3
    assert words[0] in prepositions
    assert words[1] in determiners
    assert words[2] in nouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])