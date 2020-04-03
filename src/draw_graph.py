import sys
import math
from src.calculate_values import get_values
from PIL import Image, ImageDraw

BORDER_WIDTH = 5
COLUMN_WIDTH = 10


# This probably belongs in another file that is a logic module
# and not a drawing module

#TODO: allow users to generate graphs with custom number of columns
# calculated using num*2*10
def get_image_size(size):
    switcher = {
        "s": 300,
        "m": 600,
        "l": 1200,
    }

# numbers generated may be equal to graph size, when drawing range
# it is  likely 0 to graphsize-1. 
def draw_graph(size, case):
    background_color = (225, 225, 225, 1)
    size = get_image_size(size)
    num_columns = math.floor((size/COLUMN_WIDTH)/2)
    case = get_values(case, num_columns, size - (2*BORDER_WIDTH))
    graph = PIL.Image.new("RGBA", size, background_color)
    draw = ImageDraw.Draw(graph)
    draw_border(graph)
    draw_bars(graph)
    graph.save(sys.stdout, "graph.png")

def draw_border(image):
    draw = ImageDraw.Draw(image)
    width = image.width
    height = image.height
    border_color = (0, 0, 0, 1)
    top_coords = [(0,0), (width, 0)]
    bottom_coords = [(0, height), (width, height)]
    left_coords = [(0, 0), (0, height)]
    right_coords = [(width, 0),(width, height)]
    border_coords = [top_coords, bottom_coords, left_coords, right_coords]
    for coordinates in border_coords:
      draw.line(coordinates, fill=border_color, width=BORDER_WIDTH)

# pointer color (243, 33, 45, 0)
# finished sorting color (33, 45, 243)
def draw_bars(image, values):
    draw = ImageDraw.Draw(image)
    width = image.width
    height = image.height
    bar_color = (33, 150, 243, 0)
    bar_base_height = height - BORDER_WIDTH
    x_coord = BORDER_WIDTH +1
    for val in values:
# TODO: fill out pre/post conditions for everything
# to ensure that this is never passed a value that is
# greater than the drawing range i.e. border to border.