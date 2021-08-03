import math
from typing import List, Tuple
from src.gif_generator import GifStrategy, Step, Change


class MergeSort(GifStrategy):

    def generate_steps(self,
                       values: List[int],
                       position: int = 0) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Merge Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        return self.merge_sort(values, 0)[1]

    def merge_sort(self, values: List[int],
                   position: int) -> Tuple[List[int], List[Step]]:
        """
        helper function for generate_steps

        Args:
            values (List[int]): the values to be sorted
            positon (int): the offset of the current sub-list values within
            the original list

        Returns:
            output ((List[int], List[Step])): the sorted values and the list
            of steps used
        """
        steps = []
        if len(values) < 2:
            sort = Change("color", ["sorted", position])
            steps.append(Step(position, [sort]))
            return (values, steps)
        middle = math.ceil(len(values) / 2)
        left_values = values[:middle]
        right_values = values[middle:]

        # LEFT SIDE
        # fade the right side
        right_fade_vals = list(range(position + middle, position + len(values)))
        right_fade_vals.insert(0, "fade")
        fade_right = Change("color", right_fade_vals)
        steps.append(Step(position, [fade_right]))
        # recurse, update values, and add steps
        left_output = self.merge_sort(left_values, position)
        left_values = left_output[0]
        steps.extend(left_output[1])
        # unfade and unsort
        unfade_vals = list(range(position, position + len(values)))
        unfade_vals.insert(0, "bar")
        unfade = Change("color", unfade_vals)
        steps.append(Step(position, [unfade]))

        # RIGHT SIDE
        # fade the left side
        left_fade_vals = list(range(position, position + middle))
        left_fade_vals.insert(0, "fade")
        fade_left = Change("color", left_fade_vals)
        steps.append(Step(position + middle, [fade_left]))
        # recurse, update values, and add steps
        right_output = self.merge_sort(right_values, position + middle)
        right_values = right_output[0]
        steps.extend(right_output[1])
        # unfade all
        steps.append(Step(position, [unfade]))

        # MERGE
        merge_output = self.merge(left_values, right_values, position)
        merge_steps = merge_output[1]
        steps.extend(merge_steps)
        # update values
        values = merge_output[0]
        return (values, steps)

    def merge(self, left: List[int], right: List[int],
              position: int) -> Tuple[List[int], List[Step]]:
        """
        helper function for merge_sort, merges two sorted lists

        Args:
            left (List[int]): one set of sorted values
            right (List[int]): the other set of sorted values
            positon (int): the offset of the current sub-list values within
            the original list

        Returns:
            output ((List[int], List[Step])): the sorted values and the list
            of steps used
        """
        merged = []
        steps = []
        sorted_steps = []
        i, j = 0, 0
        while len(merged) < len(left) + len(right):
            cursor = position + i + j
            left_cursor = position + i
            right_cursor = position + len(left) - 1 + j
            add_right_cursor = Change("add_cursor", [right_cursor])
            remove_right_cursor = Change("remove_cursor", [right_cursor])
            steps.append(Step(left_cursor, [add_right_cursor]))
            if j == len(right) or (i != len(left) and left[i] < right[j]):
                merged.append(left[i])
                overlay = Change("overlay", [cursor, left[i]])
                steps.append(Step(cursor, [remove_right_cursor, overlay]))
                i += 1
            else:
                merged.append(right[j])
                overlay = Change("overlay", [cursor, right[j]])
                steps.append(Step(cursor, [remove_right_cursor, overlay]))
                j += 1
            # color in the newly selected value and remove the right cursor
            fill = Change("color", ["sorted", cursor])
            sorted_steps.append(Step(cursor, [fill]))
        for step in sorted_steps:
            steps.append(step)
        return (merged, steps)


class InPlaceMergeSort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using In-place Merge
        Sort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError


class Quadsort(GifStrategy):

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Quadsort

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.

        TODO: implement
        """
        return NotImplementedError
