from typing import List
from src.gif_strategy import GifStrategy, Step, Change
from copy import copy

class InsertionSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Insertion Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        start = Change("color", ["sorted", 0])
        steps.append(Step(0, [start])) 
        for i in range(1, len(values)): 
            # set the next unsorted value as insert
            insert = values[i] 
            steps.append(Step(i))
            j = i-1
            # move sorted values that are greater than insert forwards
            while j >= 0 and insert < values[j]: 
                    values[j + 1] = values[j] 
                    erase = Change("draw", [j, 0])
                    draw  = Change("draw", [j+1, values[j]])
                    sort = Change("color", ["sorted", j+1])
                    steps.append(Step(j, [erase, draw, sort]))
                    j -= 1
            # place insert in the correct position
            values[j + 1] = insert 
            draw = Change("draw", [j+1, insert])
            sort = Change("color", ["sorted", j+1])
            steps.append(Step(j+1, [draw, sort]))
        return steps

class ShellSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Shell Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError

class CubeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Cube Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError

class BinaryTreeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Binary Tree Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError

class CycleSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Cycle Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError

class LibrarySort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Library Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError