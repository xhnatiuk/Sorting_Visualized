from abc import ABC, abstractmethod
from typing import List

class Change:
    """
    Class for defining changes that have taken place during sorting
    indentifier: draw, overlay, exchange, add_cursor, remove_cursor, color(sorted, bar, fade)
    """
    indentifier: str
    involved: List[int]

    def __init__(self, indentifier: str, involved: List[int]):
        """
        Change class constructor

        Args:
            indentifier (str): the indentifier of the change applied
            involved (List[int]): values involved in the change
        """
        self.type = indentifier
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