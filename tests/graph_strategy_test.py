from typing import List, Callable
from src.graph_strategy import *

def simple(strategy: GraphStrategy, expected: List[int]):
    actual = strategy.generate_values(5, 5)
    assert actual == expected

def duplicate_maximums(strategy: GraphStrategy, expected: List[int]):
    actual = strategy.generate_values (5, 11)
    assert actual == expected

def duplicate_zeros(strategy: GraphStrategy, expected: List[int]):
    actual = strategy.generate_values(5, 2)
    assert actual == expected
    
def empty(strategy: GraphStrategy):
    expected = []
    actual = strategy.generate_values(0, 5)
    assert actual == expected

def zero_height(strategy: GraphStrategy):
    expected = [0, 0, 0, 0, 0]
    actual = strategy.generate_values(5, 0)
    assert actual == expected

# test does not assert anything because results are unpredictable
# just makes sure code can run
def big(strategy: GraphStrategy, expected: List[int]):
    actual = strategy.generate_values (20, 100)
    # uncomment to view test results of generators with unpredictable results
    # assert actual == expected
    
class TestIncreasing:
    strategy = Increasing()

    def test_empty(self):
        empty(self.strategy)

    def test_zero_height(self):
        zero_height(self.strategy)

    def test_simple(self):
        expected = [1, 2, 3, 4, 5]
        simple(self.strategy, expected)
    
    def test_duplicate_maximums(self):
        expected = [2, 4, 6, 8, 10]
        duplicate_maximums(self.strategy, expected)
    
    def test_duplicate_zeros(self):
         expected = [0, 0, 0, 1, 2]
         duplicate_zeros(self.strategy, expected)

class TestDecreasing:
    strategy = Decreasing()

    def test_empty(self):
        empty(self.strategy)

    def test_zero_height(self):
        zero_height(self.strategy)

    def test_simple(self):
        expected = [5, 4, 3, 2, 1]
        simple(self.strategy, expected)

    def test_duplicate_maximums(self):
        expected = [10, 8, 6, 4, 2]
        duplicate_maximums(self.strategy, expected)

    def test_duplicate_zeros(self):
        expected = [2, 1, 0, 0, 0]
        duplicate_zeros(self.strategy, expected)

class TestNearlySorted:
    strategy = NearlySorted()

    def test_empty(self):
        empty(self.strategy)
    
    def test_zero_height(self):
        zero_height(self.strategy)

    def test_big(self):
        big(self.strategy, [])

class TestFewUnique:
    strategy = FewUnique()
    
    def test_empty(self):
        empty(self.strategy)

    def test_zero_height(self):
        zero_height(self.strategy)

    def test_big(self):
      big(self.strategy, [])

class TestRandom:
    strategy = Random()

    def test_empty(self):
        empty(self.strategy)

    def test_zero_height(self):
        zero_height(self.strategy)

    def test_big(self):
        big(self.strategy, [])
