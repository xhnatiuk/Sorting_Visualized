from typing import List
from src.gif_generator import GifStrategy, Step, Change


class SelectionSort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Selection Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        for i in range(len(values)):
            steps.append(Step(i))
            # set the next unsorted value as the min
            minimum_index = i
            for j in range(i + 1, len(values)):
                steps.append(Step(j))
                # if some value is smaller than the min, update the min
                if values[minimum_index] > values[j]:
                    minimum_index = j
            # swap the minimum to the front
            values[i], values[minimum_index] = values[minimum_index], values[i]
            exchange = Change("exchange", [i, minimum_index])
            sort = Change("color", ["sorted", i])
            steps.append(Step(i, [exchange, sort]))
        return steps


class Heapsort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Heapsort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        
        TODO: implement
        """
        return NotImplementedError


class Smoothsort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Smoothsort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError


class Strandsort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Strandsort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError


class TournamentSort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Tournament Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError
