import math
import random

#TODO: values calculated are going to be bad using this method...
# on graph size 1000 with 50 columns they will be hiehgts 950 through
# 1000. Fix so that they step down by a reasonable amount. Maybe
# make it always go to 0 for inc/dec and step down by amount
# that makes that possible. Nearly sorted will have to add that
# amount and random/few unique can ignore it.

def generate_increasing(quantity, maximum):
    """
    Generates an increasing list of quantity integers between 0 and maximum inclusive.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

    Returns:
        values(List[int]): a increasing list of integers.
    """
    values = []
    minimum = maximum - (quantity - 1)
    for x in range(quantity):
        value = max(minimum+x, 0)
        values.append(value)
    return values

def generate_decreasing(quantity, maximum):
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

def generate_nearly_sorted(quantity, maximum):
    """
    Generates a nearly sorted list of quantity integers between 0 and maximum inclusive.

    Args:
        quantity (int): the number of values to be generated.
        maximum (int): the maximum permissible value size.

    Returns:
        values(List[int]): a nearly sorted list of integers.
    """
    modifications = [-2, -1, 0, 1, 2]
    mod_weights = [7, 14, 68, 14, 7]
    values = generate_increasing(quantity, maximum)
    for x in range(quantity):
        modifier = random.choices(modifications, weights=mod_weights)[0]
        value = values[x] + modifier
        value = max(0, value)
        value = min(value, maximum)
        values[x] = value
    return values

def generate_few_unique(quantity, maximum):
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

def generate_random(quantity, maximum):
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

def generate_values(case, quantity, maximum):
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