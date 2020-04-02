import src
from src.draw_graph import *


#TODO investigate parameter passing to make sure num_cols is not mutated.
# also check if integer division is standard or if I need floor
# also how do I/python know if its an integer since to type???
# check bounds on loops obvi

def simple(generator, expected):
    actual = generator(5, 5)
    assert actual == expected

def duplicates(generator, expected):
    actual = generator(5, 2)
    assert actual == expected

def empty(generator):
    expected = []
    actual = generator(0, 5)
    assert actual == expected

def zero_height(generator):
    expected = [0, 0, 0, 0, 0]
    actual = generator(5, 0)
    assert actual == expected
    
class TestIncreasing:
    def test_simple(self):
        expected = [1, 2, 3, 4, 5]
        simple(generate_increasing, expected)
    
    def test_duplicates(self):
         expected = [0, 0, 0, 1, 2]
         duplicates(generate_increasing, expected)

    def test_empty(self):
        empty(generate_increasing)

    def test_zero_height(self):
        zero_height(generate_increasing)

class TestDecreasing:
    def test_simple(self):
        expected = [5, 4, 3, 2, 1]
        simple(generate_decreasing, expected)

    def test_duplicates(self):
        expected = [2, 1, 0, 0, 0]
        duplicates(generate_decreasing, expected)

    def test_empty(self):
        empty(generate_decreasing)

    def test_zero_height(self):
        zero_height(generate_decreasing)

class TestNearlySorted:
    def test_empty(self):
        empty(generate_nearly_sorted)
    
    def test_zero_height(self):
        zero_height(generate_nearly_sorted)

class TestFewUniques:
    def test_empty(self):
        empty(generate_few_unique)

    def test_zero_height(self):
        zero_height(generate_few_unique)

class TestPseudorandom:
    def test_empty(self):
        empty(generate_random)

    def test_zero_height(self):
        zero_height(generate_random)
