from typing import List, Callable
from src.generate_values import *


#TODO investigate parameter passing to make sure num_cols is not mutated.
# also check if integer division is standard or if I need floor
# also how do I/python know if its an integer since to type???
# check bounds on loops obvi

def simple(generator: Callable[[int, int], List[int]], expected: List[int]):
    actual = generator(5, 5)
    assert actual == expected

def duplicate_maximums(generator: Callable[[int, int], List[int]], expected: List[int]):
    actual = generator (5, 11)
    assert actual == expected

def duplicate_zeros(generator: Callable[[int, int], List[int]], expected: List[int]):
    actual = generator(5, 2)
    assert actual == expected
    
def empty(generator: Callable[[int, int], List[int]]):
    expected = []
    actual = generator(0, 5)
    assert actual == expected

def zero_height(generator: Callable[[int, int], List[int]]):
    expected = [0, 0, 0, 0, 0]
    actual = generator(5, 0)
    assert actual == expected

# test does not assert anything because results are unpredictable
# just makes sure code can run
def big(generator: Callable[[int, int], List[int]], expected: List[int]):
    actual = generator (20, 100)
    # uncomment to view test results of generators with unpredictable results
    # assert actual == expected
    
class TestIncreasing:
    def test_empty(self):
        empty(generate_increasing)

    def test_zero_height(self):
        zero_height(generate_increasing)

    def test_simple(self):
        expected = [1, 2, 3, 4, 5]
        simple(generate_increasing, expected)
    
    def test_duplicate_maximums(self):
        expected = [2, 4, 6, 8, 10]
        duplicate_maximums(generate_increasing, expected)
    
    def test_duplicate_zeros(self):
         expected = [0, 0, 0, 1, 2]
         duplicate_zeros(generate_increasing, expected)

class TestDecreasing:
    def test_empty(self):
        empty(generate_decreasing)

    def test_zero_height(self):
        zero_height(generate_decreasing)

    def test_simple(self):
        expected = [5, 4, 3, 2, 1]
        simple(generate_decreasing, expected)

    def test_duplicate_maximums(self):
        expected = [10, 8, 6, 4, 2]
        duplicate_maximums(generate_decreasing, expected)

    def test_duplicate_zeros(self):
        expected = [2, 1, 0, 0, 0]
        duplicate_zeros(generate_decreasing, expected)

class TestNearlySorted:
    def test_empty(self):
        empty(generate_nearly_sorted)
    
    def test_zero_height(self):
        zero_height(generate_nearly_sorted)

    def test_big(self):
        big(generate_nearly_sorted, [])

class TestFewUniques:
    def test_empty(self):
        empty(generate_few_unique)

    def test_zero_height(self):
        zero_height(generate_few_unique)

    def test_big(self):
      big(generate_few_unique, [])

class TestPseudorandom:
    def test_empty(self):
        empty(generate_random)

    def test_zero_height(self):
        zero_height(generate_random)

    def test_big(self):
        big(generate_random, [])
