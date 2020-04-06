import math
import random
from typing import List

def generate_increasing(quantity: int, maximum: int) -> List[int]:
    """
    Generates an increasing list of quantity integers between 0 and maximum inclusive.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

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

def generate_decreasing(quantity: int, maximum: int) -> List[int]:
    """
    Generates an decreasing list of quantity integers between 0 and maximum inclusive.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

    Returns:
        values(List[int]): a decreasing list of integers.
    """
    values = generate_increasing(quantity, maximum)
    return values[::-1]

def generate_nearly_sorted(quantity: int, maximum: int) -> List[int]:
    """
    Generates a nearly sorted list of quantity integers between 0 and maximum inclusive.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

    Returns:
        values(List[int]): a nearly sorted list of integers.
    """
    if quantity == 0:
        return []
    else:
        values = generate_increasing(quantity, maximum)
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

def generate_few_unique(quantity: int, maximum: int) -> List[int]:
    """
    Generates an list of quantity integers, between 0 and maximum inclusive, with few unique values.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

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

def generate_random(quantity: int, maximum: int) -> List[int]:
    """
    Generates a random list of quantity integers between 0 and maximum inclusive.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

    Returns:
        values(List[int]): a random list of integers.
    """
    values = []
    for col in range(quantity):
        value = random.randint(0, maximum)
        values.append(value)
    return values

def generate_values(case: str, quantity: int, maximum: int) -> List[int]:
    """
    Generates a list of quantity integers, between 0 and maximum inclusive, following a pattern.

    Args:
        case (string): one of the preset value patterns.
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

    Returns:
        values(List[int]): a list of integers.
    """
    switcher = {
        "i": generate_increasing(quantity, maximum),
        "d": generate_decreasing(quantity, maximum),
        "r": generate_random(quantity, maximum),
        "f": generate_few_unique(quantity, maximum),
        "n": generate_nearly_sorted(quantity, maximum),
    }