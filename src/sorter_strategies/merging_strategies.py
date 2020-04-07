from typing import List
from src.sort_strategy import SortStrategy, Step

class MergeSort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Merge Sort

        TODO: implement
        """
        return NotImplementedError

class InPlaceMergeSort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using In-place Merge Sort

        TODO: implement
        """
        return NotImplementedError

class Quadsort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Quadsort

        TODO: implement
        """
        return NotImplementedError