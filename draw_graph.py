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

def get_values(case, num_values, max_size):
    switcher = {
        "i": generate_increasing(num_values, max_size),
        "d": generate_decreasing(num_values, max_size),
        "r": generate_random(num_values, max_size),
        "f": generate_few_unique(num_values, max_size),
        "n": generate_nearly_sorted(num_values, max_size),
    }

def generate_increasing(num_values, max_size):
    values = []
    start = max_size - (num_values - 1)
    for col in range(start, max_size):
        values.append(col)
    return values

def generate_decreasing(num_values, max_size):
    values = generate_increasing(num_values, max_size)
    return values[::-1]

def generate_random(num_values, max_size):
    values = []
    for col in num_values:
        new_value = random.randint(0, max_size)
        values.append(new_value)
    return values

def generate_few_unique(num_values, max_size):
    val1 = max_size
    val2 = max_size/2
    val3 = max_size/3
    val4 = max_size/4
    return random.sample([val1, val2, val3, val4], num_values)

def generate_nearly_sorted(num_values, max_size):
    values = generate_increasing(num_values, max_size)
    for col in num_values:
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
