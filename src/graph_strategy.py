import math
import random
from typing import List
from abc import ABC, abstractmethod

class GraphStrategy(ABC):
    """
    Interface that declares contract for concrete graph strategy classes
    """

    @abstractmethod
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        """
        Generates a list of quantity integers between 0 and maximum inclusive.

        Args:
            quantity (int): the number of values to be generated.
            maximum (int): the maximum permissible value size.

        Returns:
            values(List[int]): a list of integers.
        """
        pass

class Increasing(GraphStrategy):
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        """
        Fufuills the GraphStrategy.generate_steps contract

        Returns:
            values(List[int]): a increasing list of integers.
        """
        if quantity == 0:
            return []
        else:
            values = []
            step_amount = 1
            # if more values than numbers initialize value to negative to generate 0s
            if (maximum - quantity) < 0:
                value = maximum - (quantity - 1)
            # otherwise calculate the difference between values to spread entire range
            else:
                step_amount = math.floor(maximum/quantity)
                value = step_amount
            for x in range(quantity):
                if (value < 0):
                    values.append(0)
                else:
                    values.append(value)
                value = value + step_amount
            return values

class Decreasing(GraphStrategy):
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        """
        Fufuills the GraphStrategy.generate_steps contract

        Returns:
            values(List[int]): a decreasing list of integers.
        """
        generator = Increasing()
        values = generator.generate_values(quantity, maximum)
        return values[::-1]

class NearlySorted(GraphStrategy):
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        """
        Fufuills the GraphStrategy.generate_steps contract

        Returns:
            values(List[int]): a nearly sorted list of integers.
        """
        if quantity == 0:
            return []
        else:
            generator = Increasing()
            values = generator.generate_values(quantity, maximum)
            # calculate the difference between values and use it to create modifications
            step = max(1, math.floor(maximum/quantity))
            modifications = [-2*step, 0, 2*step]
            mod_weights = [21, 58, 21]
            for x in range(quantity):
                modifier = random.choices(modifications, weights=mod_weights)[0]
                value = values[x] + modifier
                value = max(0, value)
                value = min(value, maximum)
                values[x] = value
            return values

class FewUnique(GraphStrategy):
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        """
        Fufuills the GraphStrategy.generate_steps contract

        Returns:
            values(List[int]): a list of integers with many repeated values.
        """
        val1 = maximum
        val2 = math.floor(maximum/2)
        val3 = math.floor(maximum/3)
        val4 = math.floor(maximum/4)
        val5 = 0
        possible_values = [val1, val2, val3, val4, val5]
        return random.choices(possible_values, k=quantity)

class Random(GraphStrategy):
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        """
        Fufuills the GraphStrategy.generate_steps contract

        Returns:
            values(List[int]): a random list of integers.
        """
        values = []
        for col in range(quantity):
            value = random.randint(0, maximum)
            values.append(value)
        return values