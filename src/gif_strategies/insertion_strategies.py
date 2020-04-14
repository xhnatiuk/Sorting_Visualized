from typing import List
from src.gif_strategy import GifStrategy, Step, Change
from copy import copy

class InsertionSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Insertion Sort
        """
        steps = []
        start = Change("s", [0])
        steps.append(Step(0, [start])) 
        for i in range(1, len(values)): 
            # set the next unsorted value as insert
            insert = values[i] 
            steps.append(Step(i))
            j = i-1
            # move sorted values that are greater than insert forwards
            while j >= 0 and insert < values[j]: 
                    values[j + 1] = values[j] 
                    exchange = Change("e", [j, j+1])
                    sort = Change("s", [j+1])
                    steps.append(Step(j, [exchange, sort]))
                    j -= 1
            # place insert in the correct position
            values[j + 1] = insert 
            exchange = Change("e", [j+1, j+1])
            steps.append(Step(j+1, [exchange]))
        return steps

class ShellSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Shell Sort

        TODO: implement
        """
        return NotImplementedError

class CubeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Cube Sort

        TODO: implement
        """
        return NotImplementedError

class BinaryTreeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Binary Tree Sort

        TODO: implement
        """
        return NotImplementedError

class CycleSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Cycle Sort

        TODO: implement
        """
        return NotImplementedError

class LibrarySort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Library Sort

        TODO: implement
        """
        return NotImplementedError