from typing import List
from src.sort_strategy import SortStrategy, Step

class PatienceSort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Patience Sort

        TODO: implement
        """
        return NotImplementedError

class BlockSort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Block Sort

        TODO: implement
        """
        return NotImplementedError

class Timsort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Timsort

        TODO: implement
        """
        return NotImplementedError