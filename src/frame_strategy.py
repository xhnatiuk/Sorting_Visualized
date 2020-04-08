from abc import ABC, abstractmethod
from typing import List

class FrameStrategy(ABC):
    """
    Interface that declares contract for concrete frame strategy classes
    """

    @abstractmethod
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        sorts the values and returns the steps used
        
        Args:
            values (List[int]): the values to be sorted

        Modifies:
            values: sorts the list in increasing order
            
        Returns:
            steps(List[Step]): the list of steps used
        """
        pass

class Step:
    """
    Class for tracking steps taken in a sorting algorithm
    """
    position: int
    swap: (int, int)

    def __init__(self, position: int, swap: (int, int) = None):
        """
        Step class constructor

        Args:
            position (int): the value being considered
            swap ((int, int)): the values swapped
        """
        self.position = position
        self.swap = swap 