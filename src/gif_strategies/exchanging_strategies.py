from typing import List
from src.gif_strategy import GifStrategy, Step, Change
from copy import copy
from numpy import math

class BubbleSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Bubble Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        num_sorted = 0
        exchange_occurred = True
        # the last value is already sorted
        while exchange_occurred:
            num_sorted += 1
            exchange_occurred = False
            sorted_vals = list(range(len(values) - num_sorted, len(values)))
            sorted_vals.insert(0, "sorted")
            sort = Change("color", sorted_vals)
            steps.append(Step(0, [copy(sort)]))
            # iterate the value before the last unsorted value
            for i in range(len(values) - num_sorted):
                steps.append(Step(i))
                # bubble-up value i
                if values[i] > values[i + 1]:
                    values[i], values[i + 1] = values[i + 1], values[i]
                    exchange = Change("exchange", [i, i+1])
                    steps.append(Step(i+1, [exchange]))
                    exchange_occurred = True
        sorted_vals = list(range(0, len(values)))
        sorted_vals.insert(0, "sorted")
        sort = Change("color", sorted_vals)
        steps.append(Step(0, [copy(sort)]))
        return steps

class CocktailSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Cocktail Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        num_iterations = 0
        exchange_occurred = True
        while exchange_occurred:
            exchange_occurred = False

            # bubble forwards
            for i in range(num_iterations, len(values)-1-num_iterations):
                if values[i] > values[i+1]:
                    values[i], values[i+1] = values[i+1], values[i]
                    exchange_occurred = True
                    exchange = Change("exchange", [i, i+1])
                    steps.append(Step(i, [exchange]))
                else:
                    steps.append(Step(i))
            last_sorted = len(values)-1 -num_iterations
            end_sort = Change("color", ["sorted", last_sorted])
            steps.append(Step(last_sorted, [end_sort]))
            
            # if no exchange occured values are sorted
            if not exchange_occurred:
                break

            # bubble backwards 
            exchange_occurred = False
            for i in range(len(values)-2-num_iterations, num_iterations-1, -1):
                if values[i] > values[i+1]:
                    values[i], values[i+1] = values[i+1], values[i]
                    exchange_occurred = True
                    exchange = Change("exchange", [i, i+1])
                    steps.append(Step(i+1, [exchange]))
                else:
                    steps.append(Step(i))
            start_sort = Change("color", ["sorted", num_iterations])
            steps.append(Step(num_iterations, [start_sort]))
            num_iterations += 1
        sorted_vals = list(range(0, len(values)))
        sorted_vals.insert(0, "sorted")
        sort = Change("color", sorted_vals)
        steps.append(Step(0, [copy(sort)]))
        return steps

class CombSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Comb Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        # k is generaly 1.3 in comb sort
        shrink = 1.3
        gap = len(values)
        exchange_occurred = True
        num_iterations = 0
        while exchange_occurred:
            gap /= shrink
            gap = math.floor(gap)
            if gap <= 1:
                exchange_occurred = False
                gap = 1
            for i in range (len(values) - gap):
                remove_cursor = Change("remove_cursor", [i+gap-1])
                add_cursor = Change("add_cursor", [i+gap])
                steps.append(Step(i, [remove_cursor, add_cursor]))
                if values[i] > values[i + gap]:
                    values[i], values[i+ gap] = values[i + gap], values[i]
                    exchange = Change("exchange", [i, i+gap])
                    steps.append(Step(i, [exchange]))
                    exchange_occurred = True
                if i == len(values) - gap - 1:
                    remove_final_cursor = Change("remove_cursor", [i+gap])
                    steps.append(Step(i, [remove_final_cursor]))
        sorted_vals = list(range(0, len(values)))
        sorted_vals.insert(0, "sorted")
        sort = Change("color", sorted_vals)
        steps.append(Step(0, [copy(sort)]))
        return steps

class GnomeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Gnome Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        i = 0
        while i < len(values):
            if (i == 0 or values[i] >= values[i-1]):
                sort = Change("color", ["sorted", i])
                steps.append(Step(i, [sort]))
                i += 1
            else:
                values[i], values[i-1] = values[i-1], values[i]
                exchange = Change("exchange", [i, i-1])
                sort = Change("color", ["sorted", i])
                steps.append(Step(i-1, [exchange, sort]))
                i -= 1
        return steps

class OddEvenSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Odd-Even Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        steps = []
        done = False
        while not done:
            done = True
            for i in range (1, len(values)-1, 2):
                if values[i] > values [i+1]:
                    values[i], values[i+1] = values[i+1], values[i]
                    exchange = Change("exchange", [i, i+1])
                    steps.append(Step(i, [exchange]))
                    done = False
                else:
                    steps.append(Step(i))
            for i in range (0, len(values)-1, 2):
                if values[i] > values [i+1]:
                    values[i], values[i+1] = values[i+1], values[i]
                    exchange = Change("exchange", [i, i+1])
                    steps.append(Step(i, [exchange]))
                    done = False
                else:
                    steps.append(Step(i))
        sorted_vals = list(range(0, len(values)))
        sorted_vals.insert(0, "sorted")
        sort = Change("color", sorted_vals)
        steps.append(Step(0, [copy(sort)]))
        return steps