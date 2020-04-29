from abc import ABC, abstractmethod
from typing import List

class Change:
    """
    Class for defining changes that have taken place during sorting
    types: 
        d: draw
        o: overlay
        e: exchange
        c: color
            s: sort
            f: fade
            u: unfade
    """
    type: str
    involved: List[int]

    def __init__(self, type: str, involved: List[int]):
        """
        Change class constructor

        Args:
            type (str): the type of change applied
            involved (List[int]): indicies of values involved in the change
        """
        self.type = type
        self.involved = involved 

class Step:
    """
    Class for tracking steps taken in a sorting algorithm
    """
    position: int
    changes: List[Change]

    def __init__(self, position: int, changes: List[Change] = None):
        """
        Step class constructor

        Args:
            position (int): the index of the value being considered
            changes (List[Change]): changes applied
        """
        self.position = position
        self.changes = changes 

class GifStrategy(ABC):
    """
    Interface that declares contract for concrete gif strategy classes
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