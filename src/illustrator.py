import sys
import math
from PIL import Image, ImageDraw
from typing import List
from src.exceptions import InputError

class ColorProfile:
    def __init__(self, background, border, bar, sorted_, cursor):
        """
        Constructor for ColorProfile class

        background (int, int, int, int): the RGBA color code for the background
        border (int, int, int, int): the RGBA color code for the border
        bar (int, int, int, int): the RGBA color code for the bar
        sorted_ (int, int, int, int): the RGBA color code for the sorted bars
        pointer (int, int, int, int): the RGBA color code for the cursor
        """
        self.background = background
        self.border = border
        self.bar = bar
        self.sorted = sorted_
        self.pointer = cursor

class Illustrator:
    def __init__(self, image_size: (int, int), border_size: (int), colors: ColorProfile) -> None:

        """
        Constructor for GraphGenerator class

        Args:
            image_size (int, int): the width and height of the image
            border_size (int): the size of the border
            colors (ColorProfile): RGBA color profile for the Illustrator
        """
        self.image_width = image_size[0]
        self.image_height = image_size[1]
        self.border_size = border_size
        self.colors = colors


    def draw_border(self, draw: ImageDraw) -> None:
        """
        Draws a 50% self._border_color border onto the image. Leaves the other half as self._background_color.

        Args:
            draw (ImageDraw): the drawing object
            
        Modifies:
            the Image pertaining to draw

        Returns:
            None
        """
        top_coords = [(0, 0), (self.image_width, 0)]
        bottom_coords = [(0, self.image_height-1), (self.image_width, self.image_height-1)]
        left_coords = [(0, 0), (0, self.image_height)]
        right_coords = [(self.image_width-1, 0),(self.image_width-1, self.image_height)]
        border_coords = [top_coords, bottom_coords, left_coords, right_coords]
        for coordinates in border_coords:
            draw.line(coordinates, fill=self.colors.border, width=self.border_size)

   
    def draw_bars(self, values: List[int], draw: ImageDraw) -> None:
        """
        Draws a bar for each value onto the image

        Args:
            values(List[int]): the values to be drawn
            draw (ImageDraw): the drawing object

        Raises:
            InputError: number of values is too large for the image size
        
        Modifies:
            the Image pertaining to draw

        Returns:
            None

        Notes:
            values greater than (height - 2*border_width) will be drawn over the border and
            capped at (height - border_width) since that is the uppermost edge of the image
        """
        num_bars = len(values)
        # drawing range divided by number of bars + white space between them
        bar_width = math.floor((self.image_width - 2*self.border_size)/(2*num_bars - 1))
        if bar_width < 1:
            raise InputError(bar_width, "Bar width cannot be less than 1")
        padding = (self.image_width - 2*self.border_size) - (bar_width*(2*num_bars -1))
        # calculate starting offset to ensure graph is centered within the border 
        x_offset = self.border_size + (padding/2) + bar_width/2
        y_offset = self.image_height - self.border_size
        for val in values:
            if val != 0:
                draw.line ([(x_offset, y_offset),(x_offset, y_offset - val)], fill=self.colors.bar, width=bar_width)
            x_offset = x_offset + (2*bar_width)

    def draw_graph(self, values: List[int], draw: ImageDraw) -> None:
        """
        Draws a graph

        Args:
            values(List[int]): a list of values
            draw (ImageDraw): the drawing object

        Raises:
            InputError: number of values is too large for the image size

        Modifies:
            the Image pertaining to draw

        Returns:
            None
        """
        self.draw_border(draw)
        self.draw_bars(values, draw)

    def erase_cursor(self, position: int, draw: ImageDraw) -> None:
        """
        erases the cursor on the image at the position

        Args:
            position (int): the index of the cursor
            draw (ImageDraw): the drawing object
        
        Modifies:
            the Image pertaining to draw

        Returns:
            None
        """
        draw_cursor(self, position, draw, self.colors.background)

    def draw_cursor(self, position: int, draw: ImageDraw, color:(int, int, int, int)=self.colors.cursor) -> None:
        """
        draws a color cursor on the image at the position

        Args:
            position (int): the index of the cursor
            draw (ImageDraw): the drawing object
            color (int, int, int, int): RGBA color code

        Modifies:
            the Image pertaining to draw

        Returns:
            None
        """

    def erase_bar(self, position: int, draw: ImageDraw) -> None:
        """
        erases the bar on the image at the position

        Args:
            position (int): the index of the bar
            value (int): the new bar value
            draw (ImageDraw): the drawing object
            color (int, int, int, int): RGBA color code

        Modifies:
            the Image pertaining to draw

        Returns:
            None
        """
        max_bar_val = self.image_height - 2*self.border_size
        draw_bar(self, position, max_bar_val, draw, self.colors.background)

    def draw_bar(self, position: int, value: int, draw: ImageDraw, color: (int, int, int, int)=self.colors.bar) -> None:
        """
        draws a color bar of the correct height on the image at the position

        Args:
            position (int): the index of the bar
            value (int): the new bar value
            draw (ImageDraw): the drawing object
            color (int, int, int, int): RGBA color code

        Modifies:
            the Image pertaining to draw

        Returns:
            None
        """

    