import math
import random

#TODO: values calculated are going to be bad using this method...
# on graph size 1000 with 50 columns they will be hiehgts 950 through
# 1000. Fix so that they step down by a reasonable amount. Maybe
# make it always go to 0 for inc/dec and step down by amount
# that makes that possible. Nearly sorted will have to add that
# amount and random/few unique can ignore it.

def generate_increasing(quantity, maximum):
    values = []
    minimum = maximum - (quantity - 1)
    for x in range(quantity):
        value = max(minimum+x, 0)
        values.append(value)
    return values

def generate_decreasing(quantity, maximum):
    values = generate_increasing(quantity, maximum)
    return values[::-1]

def generate_nearly_sorted(quantity, maximum):
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
    possible_values = [maximum, maximum/2, maximum/3, maximum/4]
    return random.choices(possible_values, k=quantity)

def generate_random(quantity, maximum):
    values = []
    for col in range(quantity):
        value = random.randint(0, maximum)
        values.append(value)
    return values

def get_values(case, quantity, maximum):
    switcher = {
        "i": generate_increasing(quantity, maximum),
        "d": generate_decreasing(quantity, maximum),
        "r": generate_random(quantity, maximum),
        "f": generate_few_unique(quantity, maximum),
        "n": generate_nearly_sorted(quantity, maximum),
    }
