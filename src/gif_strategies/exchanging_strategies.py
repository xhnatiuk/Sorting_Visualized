from typing import List
from src.gif_strategy import GifStrategy, Step, Change
from copy import copy

class BubbleSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Bubble Sort
        """
        steps = []
        num_sorted = 0
        exchange_occurred = True
        # the last value is already sorted
        while exchange_occurred:
            num_sorted += 1
            exchange_occurred = False
            sorted_vals = list(range(len(values) - num_sorted, len(values)))
            sorted_vals.insert(0, "s")
            sort = Change("c", sorted_vals)
            steps.append(Step(0, [copy(sort)]))
            # iterate the value before the last unsorted value
            for i in range(len(values) - num_sorted):
                steps.append(Step(i))
                # bubble-up value i
                if values[i] > values[i + 1]:
                    values[i], values[i + 1] = values[i + 1], values[i]
                    exchange = Change("e", [i, i+1])
                    steps.append(Step(i+1, [exchange]))
                    exchange_occurred = True
            
        return steps

class CocktailSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Cocktail Sort

        TODO: implement
        """
        return NotImplementedError

class CombSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Comb Sort

        TODO: implement
        """
        return NotImplementedError

class GnomeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Gnome Sort
        """
        steps = []
        i = 0
        while i < len(values):
            if (i == 0 or values[i] >= values[i-1]):
                sort = Change("c", ["s", i])
                steps.append(Step(i, [sort]))
                i += 1
            else:
                values[i], values[i-1] = values[i-1], values[i]
                exchange = Change("e", [i, i-1])
                sort = Change("c", ["s", i])
                steps.append(Step(i-1, [exchange, sort]))
                i -= 1
        return steps

        

class OddEvenSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Odd-Even Sort

        TODO: implement
        """
        return NotImplementedError