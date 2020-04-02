import math
import random
from PIL import Image

SIZE_SMALL = 250
SIZE_MEDIUM = 500
SIZE_LARGE = 1000
COLUMN_SIZE = 10
BACKGROUND_COLOR = (225, 225, 225, 1)

def get_image_size(size):
    switcher = {
        "s": SIZE_SMALL,
        "m": SIZE_MEDIUM,
        "l": SIZE_LARGE,
    }

def get_values(case, num_values, max_value):
    switcher = {
        "i": generate_increasing(num_values, max_value),
        "d": generate_decreasing(num_values, max_value),
        "r": generate_random(num_values, max_value),
        "f": generate_few_unique(num_values, max_value),
        "n": generate_nearly_sorted(num_values, max_value),
    }

def generate_increasing(num_values, max_value):
    values = []
    min_value = max_value - (num_values - 1)
    for i in range(num_values):
        value = max(min_value+i, 0)
        values.append(value)
    return values

def generate_decreasing(num_values, max_value):
    values = generate_increasing(num_values, max_value)
    return values[::-1]

def generate_random(num_values, max_value):
    values = []
    for col in range(num_values):
        new_value = random.randint(0, max_value)
        values.append(new_value)
    return values

def generate_few_unique(num_values, max_value):
    val1 = max_value
    val2 = max_value/2
    val3 = max_value/3
    val4 = max_value/4
    return random.sample([val1, val2, val3, val4], num_values)

def generate_nearly_sorted(num_values, max_value):
    values = generate_increasing(num_values, max_value)
    for col in range(num_values):
        if ((values[col]%5)==0):
            new_value = values[col] + random.randint(-2, 2)
            values[col] = new_value
    return values


# numbers generated may be equal to graph size, when drawing range
# is likely 0 to graphsize-1. 
def draw_graph(size, case):
    size = get_image_size(size)
    num_columns = math.floor((size/COLUMN_SIZE)/2)
    case = get_values(case, num_columns, size)
    graph = PIL.Image.new("RGBA", size, BACKGROUND_COLOR)
# TODO: draw graphs
