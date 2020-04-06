import sys
import math
from typing import List
from PIL import Image, ImageDraw
from src.exceptions import InputError

def draw_border(image: Image, draw: ImageDraw, border_width: int):
    """
    Draws a 50% border color border onto the image. Leaves the other half as background color.

    Args:
        image (Image): the image to be drawn onto
        draw (ImageDraw): the drawing object
        border-width (int): weight of the image's border
        
    Modifies:
        image

    Notes:
        non-even values for border_width do not draw balanced borders
    """
    width = image.width
    height = image.height
    border_color = (0, 0, 0, 255)
    top_coords = [(0, 0), (width, 0)]
    bottom_coords = [(0, height-1), (width, height-1)]
    left_coords = [(0, 0), (0, height)]
    right_coords = [(width-1, 0),(width-1, height)]
    border_coords = [top_coords, bottom_coords, left_coords, right_coords]
    for coordinates in border_coords:
      draw.line(coordinates, fill=border_color, width=border_width)

# pointer color (243, 33, 45, 0)
# finished sorting color (33, 45, 243)
def draw_bars(values: List[int], image: Image, draw: ImageDraw, border_width: int):
    """
    Draws a bar for each value onto the image
    Args:
        values(List[int]): the values to be drawn
        image (Image): the image to be drawn onto
        draw (ImageDraw): the drawing object
        border-width (int): weight of the image's border

    Raises:
        InputError: number of values is too large and cannot be drawn
    
    Modifies:
        image

    Notes:
        values greater than (height - 2*border_width) will be drawn over the border and
        capped at (height - border_width) since that is the uppermost edge of the image
    """
    num_bars = len(values)
    bar_color = (33, 150, 243, 255)
    # drawing range divided by number of bars + white space between them
    bar_width = math.floor((image.width - 2*border_width)/(2*num_bars - 1))
    if bar_width < 1:
        raise InputError(bar_width, "Bar width cannot be less than 1")
    padding = (image.width - 2*border_width) - (bar_width*(2*num_bars -1))
    # calculate starting offset to ensure graph is centered within the border 
    x_offset = border_width + (padding/2) + bar_width/2
    y_offset = image.height - border_width
    for val in values:
        if val != 0:
            draw.line ([(x_offset, y_offset),(x_offset, y_offset - val)], fill=bar_color, width=bar_width)
        x_offset = x_offset + (2*bar_width)

# numbers generated may be equal to graph size, when drawing range
# it is  likely 0 to graphsize-1.
def draw_graph(values: List[int], img_size: int, border_width: int, file_path: str):
    """
    Draws a graph
    Args:
        values(List[int]): a list of values
        size (int): height and width of image in pixels
        border-width (int): weight of the image's border
        file_path (string): the path relative to ./out to save the graph to

    Raise:
        InputError: img_size < 1 OR len(value) < 1

    Modifies
        ./out
    """
    if img_size < (1, 1):
        raise InputError(img_size, "image size cannot be less than 1")
    if len(values) < 1:
        raise InputError(len(values), "cannot draw graph with less than 1 value")
    background_color = (255, 255, 900, 255)
    graph = Image.new("RGBA", img_size, background_color)
    draw = ImageDraw.Draw(graph)
    draw_border(graph, draw, border_width)
    draw_bars(values, graph, draw, border_width)
    fp = "./out/"+file_path+".png"
    graph.save(fp)
