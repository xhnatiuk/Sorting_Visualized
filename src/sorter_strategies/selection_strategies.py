from typing import List
from src.sort_strategy import SortStrategy, Step

class SelectionSort(SortStrategy):

    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Selection Sort
        """

        steps = []
        for i in range (len(values)):
            steps.append(Step(i))
            minimum_index = i
            for j in range (i+1, len(values)):
                steps.append(Step(j))
                if values[minimum_index] > values[j]:
                    minimum_index = j
            values[i], values[minimum_index] = values[minimum_index], values[i]
            steps.append(Step(i, (i ,minimum_index)))
        return steps

class Heapsort(SortStrategy):

    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Heapsort
        
        TODO: implement
        """
        return NotImplementedError

class Smoothsort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Smoothsort

        TODO: implement
        """
        return NotImplementedError


class Strandsort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Strandsort

        TODO: implement
        """
        return NotImplementedError

class TournamentSort(SortStrategy):
    def sort(self, values: List[int]) -> List[Step]:
        """
        Fufuills the SortStrategy.sort contract using Tournament Sort

        TODO: implement
        """
        return NotImplementedError
