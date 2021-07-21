"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest
from textwrap import wrap


def no_duplicates(a_string):
    return ''.join(sorted(set(a_string.lower())))


def reversed_words(a_string):
    x = ' '.join(list(reversed(a_string.split())))
    return x.split()


def four_char_strings(a_string):
    return wrap(a_string, 4)


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', 'circ', 'us']


a_string = 'monty pythons flying circus'

print(no_duplicates(a_string))
print((reversed_words(a_string)))
print(four_char_strings(a_string))
test_no_duplicates()
test_reversed_words()
test_four_char_strings()


