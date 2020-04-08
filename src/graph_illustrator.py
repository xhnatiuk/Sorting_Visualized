import sys
import math
from PIL import Image, ImageDraw
from typing import List
from src.exceptions import InputError

class ColorProfile:
    def __init__(self, background, border, bar, sorted_, cursor):
        """
        Constructor for ColorProfile class.

        background (int, int, int, int): the RGBA color code for the background.
        border (int, int, int, int): the RGBA color code for the border.
        bar (int, int, int, int): the RGBA color code for the bar.
        sorted_ (int, int, int, int): the RGBA color code for the sorted bars.
        cursor (int, int, int, int): the RGBA color code for the cursor.
        """
        self.background = background
        self.border = border
        self.bar = bar
        self.sorted = sorted_
        self.cursor = cursor

class GraphIllustrator:
    def __init__(self, num_bars: int,  image_size: (int, int), border_size: int, colors: ColorProfile) -> None:

        """
        Constructor for GraphIllustrator class.

        Args:
            image_size (int, int): the width and height of the image.
            border_size (int): the size of the border.
            colors (ColorProfile): RGBA color profile for the GraphIllustrator.
        """
        self.image_width = image_size[0]
        self.image_height = image_size[1]
        self.border_size = border_size
        self.bar_width = math.floor((self.image_width - 2*self.border_size)/(2*num_bars - 1))
        self.padding = (self.image_width - 2*self.border_size) - (self.bar_width*(2*num_bars -1))
        self.colors = colors


    def draw_border(self, draw: ImageDraw) -> None:
        """
        Draws a 50% self._border_color border onto the image. Leaves the other half as self._background_color.

        Args:
            draw (ImageDraw): the drawing object.
            
        Modifies:
            the Image pertaining to draw.

        Returns:
            None.
        """
        top_coords = [(0, 0), (self.image_width, 0)]
        bottom_coords = [(0, self.image_height-1), (self.image_width, self.image_height-1)]
        left_coords = [(0, 0), (0, self.image_height)]
        right_coords = [(self.image_width-1, 0),(self.image_width-1, self.image_height)]
        border_coords = [top_coords, bottom_coords, left_coords, right_coords]
        for coordinates in border_coords:
            draw.line(coordinates, fill=self.colors.border, width=self.border_size)

    def draw_cursor(self, position: int, draw: ImageDraw, color:(int, int, int, int)) -> None:
        """
        draws a color cursor on the image at the position.

        Args:
            position (int): the index of the cursor.
            draw (ImageDraw): the drawing object.
            color (int, int, int, int): RGBA color code.

        Modifies:
            the Image pertaining to draw.

        Returns:
            None.
        """
        cursor_width = self.bar_width
        x_start = self.border_size + math.ceil(self.padding/2)
        cursor_center = x_start + (2*self.bar_width)*position  + math.floor(self.bar_width/2)          
        max_left_bound = x_start + (2*self.bar_width)*position
        max_right_bound = max_left_bound + self.bar_width
        top_bound = self.image_height - self.border_size + 1
        bottom_bound = self.image_height - math.ceil(self.border_size/2)

        points = []
        left_bound = cursor_center
        right_bound = cursor_center + 1
        for y in range (top_bound, bottom_bound):
            left_bound = max(max_left_bound, left_bound)
            right_bound = min(max_right_bound, right_bound)
            for x in range (left_bound, right_bound):
                points.append((x, y))
            left_bound = left_bound - 1
            right_bound = right_bound + 1
        draw.point(points, color)

    def erase_cursor(self, position: int, draw: ImageDraw) -> None:
        """
        erases the cursor on the image at the position.

        Args:
            position (int): the index of the cursor.
            draw (ImageDraw): the drawing object.
        
        Modifies:
            the Image pertaining to draw.

        Returns:
            None.
        """
        draw_cursor(self, position, draw, self.colors.background)

    def draw_bar(self, position: int, value: int, draw: ImageDraw, color: (int, int, int, int)) -> None:
        """
        draws a color bar of the correct height on the image at the position.

        Args:
            position (int): the index of the bar.
            value (int): the new bar value.
            draw (ImageDraw): the drawing object.
            color (int, int, int, int): RGBA color code.

        Modifies:
            the Image pertaining to draw.

        Raises:
            InputError: number of values is too large for the image size.

        Returns:
            None.

        Notes:
            values greater than (height - 2*border_width) will be drawn over the border and
            capped at (height - border_width) since that is the uppermost edge of the image.
        """
        # drawing range divided by number of bars + white space between them
        if self.bar_width < 1:
            raise InputError(self.bar_width, "bar_width cannot be less than 1")
        # calculate starting offset to ensure graph is centered within the border 
        x_start = self.border_size + math.ceil(self.padding/2) + math.floor(self.bar_width/2)
        x_offset = x_start + (2*self.bar_width)*position
        y_offset = self.image_height - self.border_size
        if value != 0:
            draw.line ([(x_offset, y_offset),(x_offset, y_offset - value)], fill=color, width=self.bar_width)


    def erase_bar(self, position: int, draw: ImageDraw) -> None:
        """
        erases the bar on the image at the position.

        Args:
            position (int): the index of the bar.
            value (int): the new bar value.
            draw (ImageDraw): the drawing object.
            color (int, int, int, int): RGBA color code.

        Modifies:
            the Image pertaining to draw.

        Returns:
            None.
        """
        max_bar_val = self.image_height - 2*self.border_size
        draw_bar(self, position, max_bar_val, draw, self.colors.background)

    def draw_bars(self, values: List[int], draw: ImageDraw) -> None:
        """
        Draws a bar for each value onto the image.

        Args:
            values(List[int]): the values to be drawn.
            draw (ImageDraw): the drawing object.

        Raises:
            InputError: number of values is too large for the image size.
        
        Modifies:
            the Image pertaining to draw.

        Returns:
            None.
        """
        for i in range(len(values)):
            self.draw_bar(i, values[i], draw, self.colors.bar)

    def draw_graph(self, values: List[int], draw: ImageDraw) -> None:
        """
        Draws a graph

        Args:
            values(List[int]): a list of values.
            draw (ImageDraw): the drawing object.

        Raises:
            InputError: 
                * number of values is too large for the image size.
                * no values are passed.

        Modifies:
            the Image pertaining to draw.

        Returns:
            None.
        """
        if len(values) < 1:
            raise InputError(len(values), "cannot draw a graph with no data")
        self.draw_border(draw)
        self.draw_bars(values, draw)