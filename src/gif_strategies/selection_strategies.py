from typing import List
from src.gif_strategy import GifStrategy, Step, Change

class SelectionSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Selection Sort
        """
        steps = []
        for i in range (len(values)):
            steps.append(Step(i))
            # set the next unsorted value as the min
            minimum_index = i
            for j in range (i+1, len(values)):
                steps.append(Step(j))
                # if some value is smaller than the min, update the min
                if values[minimum_index] > values[j]:
                    minimum_index = j
            # swap the minimum to the front
            values[i], values[minimum_index] = values[minimum_index], values[i]
            exchange = Change("e", [i, minimum_index])
            sort = Change("s", [i])
            steps.append(Step(i, [exchange, sort]))
        return steps

class Heapsort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Heapsort
        
        TODO: implement
        """
        return NotImplementedError

class Smoothsort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Smoothsort

        TODO: implement
        """
        return NotImplementedError


class Strandsort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Strandsort

        TODO: implement
        """
        return NotImplementedError

class TournamentSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Tournament Sort

        TODO: implement
        """
        return NotImplementedError
