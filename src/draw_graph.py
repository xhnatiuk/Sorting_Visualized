import sys
import math
from PIL import Image, ImageDraw

# allows for easy extendability for user input by evaluating the length of their input
def calculate_column_size(num_cols, width):
    """
    Calculates the largest possible column size. 

    Args:
        nums_cols (int): the number of columns to be drawn
        width (int): the width of the drawing range

    Returns:
        column_size (int): the width of a column
    """

def draw_border(image, draw, border_width):
    """
    Draws a border onto the image

    Args:
        image (Image): the image to be drawn onto
        draw (ImageDraw): the drawing object
        border-width (int): weight of the image's border
        
    TODO: 
        * determine how to write that it modifies the image
    """
    width = image.width
    height = image.height
    border_color = (0, 0, 0, 1)
    top_coords = [(0,0), (width, 0)]
    bottom_coords = [(0, height), (width, height)]
    left_coords = [(0, 0), (0, height)]
    right_coords = [(width, 0),(width, height)]
    border_coords = [top_coords, bottom_coords, left_coords, right_coords]
    for coordinates in border_coords:
      draw.line(coordinates, fill=border_color, width=border_width)

# pointer color (243, 33, 45, 0)
# finished sorting color (33, 45, 243)
def draw_bars(values, image, draw, border_width):
    """
    Draws a column for each value onto the image
    Args:
        values(List[int]): the values to be drawn
        image (Image): the image to be drawn onto
        draw (ImageDraw): the drawing object
        border-width (int): weight of the image's border

    TODO: 
        * determine how to write that it modifies the image & that it expects nothing
          to be outside of the drawing range because it will not scale the values.
    """
    width = image.width
    height = image.height
    num_columns = len(values)
    bar_color = (33, 150, 243, 0)
    bar_base_height = height - border_width
    x_coord = border_width + 1
    for val in values:

# numbers generated may be equal to graph size, when drawing range
# it is  likely 0 to graphsize-1. 
def draw_graph(values, img_size, border_width):
    """
    Draws a graph
    Args:
        values(List[int]): a list of values
        size (int): height and width of image in pixels
        border-width (int): weight of the image's border

    TODO: 
        * determine what this returns
    """
    background_color = (225, 225, 225, 1)
    graph = PIL.Image.new("RGBA", img_size, background_color)
    draw = ImageDraw.Draw(graph, draw)
    draw_border(graph, draw, border_width)
    draw_bars(values, graph, draw, border_width)
    graph.save(sys.stdout, "graph.png")