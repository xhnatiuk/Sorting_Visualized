import math
from PIL import ImageDraw
from typing import List, Tuple
from .exceptions import InputError


class ColorProfile:
    """
    Class for storing all the RGB color codes for drawing a bar graph.

    Attributes:
        background (int, int, int): the RGB color code for the background.
        border (int, int, int): the RGB color code for the border.
        bar (int, int, int): the RGB color code for the bar.
        fade (int, int, int): the RGB color code for a faded bar.
        finished (int, int, int): the RGB color code for the sorted bars.
        cursor (int, int, int): the RGB color code for the cursor.
    """

    def __init__(self, background: Tuple[int, int, int], border: Tuple[int, int,
                                                                       int],
                 bar: Tuple[int, int, int], fade: Tuple[int, int, int],
                 finished: Tuple[int, int, int], cursor: Tuple[int, int, int]):
        """
        Constructor for ColorProfile class.

        background (int, int, int): RGB color for thebackground.
        border (int, int, int): RGB color for the border.
        bar (int, int, int): RGB color for bars.
        fade (int, int, int): RGB color for faded bars.
        finished (int, int, int): RGB color for sorted bars.
        cursor (int, int, int): RGB color for cursors.
        """
        self.background = background
        self.border = border
        self.bar = bar
        self.fade = fade
        self.finished = finished
        self.cursor = cursor


class GraphIllustrator:
    """
    Class for drawing and editing bar graphs.

    Attributes:
        image_width (int): the width of the image in pixels
        image_height (int): the  height of the image in pixels
        border_size (int): the width of the border in pixels
        num_bars (int): the number of bars in the graph
        bar_width (int): the width of a bar in pixels
        padding (int): the horizontal padding between the border and the first
        and last bars in pixels
        colrs (ColorProfile): the object used to select colors for drawing
    """

    def __init__(self, num_bars: int, image_size: Tuple[int, int],
                 border_size: int, colors: ColorProfile) -> None:
        """
        Constructor for GraphIllustrator class.

        Args:
            image_size (int, int): the width and height of the image.
            border_size (int): the size of the border.
            colors (ColorProfile): RGB color profile for the GraphIllustrator.
        """
        self.image_width = image_size[0]
        self.image_height = image_size[1]
        self.border_size = border_size
        self.num_bars = num_bars
        self.bar_width = (self.image_width -
                          2 * self.border_size) // (2 * num_bars - 1)
        self.padding = (self.image_width -
                        2 * self.border_size) - (self.bar_width *
                                                 (2 * num_bars - 1))
        self.colors = colors

    def draw_cursor(self, position: int, draw: ImageDraw,
                    color: Tuple[int, int, int]) -> None:
        """
        draws a color cursor on the image at the position.

        Args:
            position (int): the index of the cursor.
            draw (ImageDraw): the drawing object.
            color (int, int, int, int): RGB color code.

        Modifies:
            draw: a color cursor is drawn onto the image associated with the
            drawing object.

        Returns:
            None.
        """
        if position < 0 or position > (self.num_bars - 1):
            raise InputError((position), "invalid cursor position")

        x_start = self.border_size + math.ceil(self.padding / 2)
        cursor_center = x_start + (
            2 * self.bar_width) * position + self.bar_width // 2
        max_left_bound = x_start + (2 * self.bar_width) * position
        max_right_bound = max_left_bound + self.bar_width
        top_bound = self.image_height - self.border_size + 1
        bottom_bound = self.image_height - math.ceil(self.border_size / 2)

        points = []
        left_bound = cursor_center
        right_bound = cursor_center + 1
        for y in range(top_bound, bottom_bound):
            left_bound = max(max_left_bound, left_bound)
            right_bound = min(max_right_bound, right_bound)
            for x in range(left_bound, right_bound):
                points.append((x, y))
            left_bound = left_bound - 1
            right_bound = right_bound + 1
        draw.point(points, color)

    def erase_cursor(self, position: int, draw: ImageDraw) -> None:
        """
        Erases the cursor on the image at the position.

        Args:
            position (int): the index of the cursor.
            draw (ImageDraw): the drawing object.

        Modifies:
            draw: a cursor is erased from the image associated with the
            drawing object.

        Returns:
            None.
        """
        self.draw_cursor(position, draw, self.colors.background)

    def draw_bar(self, position: int, value: int, draw: ImageDraw,
                 color: Tuple[int, int, int]) -> None:
        """
        Draws a color bar of the correct height on the image at the position.

        Args:
            position (int): the index of the bar.
            value (int): the new bar value.
            draw (ImageDraw): the drawing object.
            color (int, int, int, int): RGB color code.

        Modifies:
            draw: a bar is drawn onto the image associated with the drawing
            object.

        Raises:
            InputError: number of values is too large for the image size.

        Returns:
            None.
        """
        if position < 0 or position > (self.num_bars - 1):
            raise InputError((position), "invalid bar position")
        if value < 0 or value > (self.image_height - 2 * self.border_size):
            raise InputError((value), "invalid bar value")
        # drawing range divided by number of bars + white space between them
        if self.bar_width < 1:
            raise InputError(self.bar_width, "bar_width cannot be less than 1")
        # calculate starting offset to ensure graph is centered within the
        # border
        x_start = self.border_size + math.ceil(
            self.padding / 2) + self.bar_width // 2
        x_offset = x_start + (2 * self.bar_width) * position
        y_offset = self.image_height - self.border_size
        if value != 0:
            draw.line([(x_offset, y_offset), (x_offset, y_offset - value)],
                      fill=color,
                      width=self.bar_width)

    def erase_bar(self, position: int, draw: ImageDraw) -> None:
        """
        Erases the bar on the image at the position.

        Args:
            position (int): the index of the bar.
            draw (ImageDraw): the drawing object.

        Modifies:
            draw: a bar is erased from the image associated with the drawing
            object.

        Returns:
            None.
        """
        max_bar_val = self.image_height - 2 * self.border_size
        self.draw_bar(position, max_bar_val, draw, self.colors.background)

    def draw_bar_outline(self, position: int, value: int, draw: ImageDraw,
                         color: Tuple[int, int, int]):
        if position < 0 or position > (self.num_bars - 1):
            raise InputError((position), "invalid bar position")
        if value < 0 or value > (self.image_height - 2 * self.border_size):
            raise InputError((value), "invalid bar value")
        # drawing range divided by number of bars + white space between them
        if self.bar_width < 1:
            raise InputError(self.bar_width, "bar_width cannot be less than 1")
        # calculate starting offset to ensure graph is centered within the
        # border
        x_start = self.border_size + math.ceil(
            self.padding / 2) + self.bar_width // 2
        x_offset = x_start + (2 * self.bar_width) * position
        y_offset = self.image_height - self.border_size
        line_offset = self.bar_width // 2
        if value != 0:
            draw.line([(x_offset - line_offset, y_offset),
                       (x_offset - line_offset, y_offset - value)],
                      fill=color,
                      width=1)
            draw.line([(x_offset + line_offset - 1, y_offset),
                       (x_offset + line_offset - 1, y_offset - value)],
                      fill=color,
                      width=1)
            draw.line([(x_offset - line_offset, y_offset - value),
                       (x_offset + line_offset - 1, y_offset - value)],
                      fill=color,
                      width=1)

    def draw_bars(self, values: List[int], draw: ImageDraw) -> None:
        """
        Draws a bar for each value onto the image.

        Args:
            values(List[int]): the values to be drawn.
            draw (ImageDraw): the drawing object.

        Raises:
            InputError: number of values is too large for the image size.

        Modifies:
            draw: a bar is drawn onto the image associated with the drawing
            object for each value in values.

        Returns:
            None.
        """
        for i in range(len(values)):
            self.draw_bar(i, values[i], draw, self.colors.bar)

    def draw_border(self, draw: ImageDraw) -> None:
        """
        Draws a half self.colors.border, half self.colors.background border
        onto the image.

        Args:
            draw (ImageDraw): the drawing object.

        Modifies:
            draw: a border is drawn onto the image associated with the drawing
            object.

        Returns:
            None.
        """
        if self.border_size < 0 or self.border_size > min(
                self.image_height, self.image_width):
            raise InputError(
                self.border_size,
                """border size cannot be negative or more than the image's
                 minimum dimension""")
        top_coords = [(0, 0), (self.image_width, 0)]
        bottom_coords = [(0, self.image_height - 1),
                         (self.image_width, self.image_height - 1)]
        left_coords = [(0, 0), (0, self.image_height)]
        right_coords = [(self.image_width - 1, 0),
                        (self.image_width - 1, self.image_height)]
        border_coords = [top_coords, bottom_coords, left_coords, right_coords]
        for coordinates in border_coords:
            draw.line(coordinates,
                      fill=self.colors.border,
                      width=self.border_size)

    def draw_graph(self, values: List[int], draw: ImageDraw) -> None:
        """
        Draws a bar graph of the values in values

        Args:
            values(List[int]): a list of values.
            draw (ImageDraw): the drawing object.

        Raises:
            InputError:
                * number of values is too large for the image size.
                * no values are passed.

        Modifies:
            draw: a bar graph is drawn onto the image associated with the
            drawing object.

        Returns:
            None.
        """
        if len(values) < 1:
            raise InputError(len(values), "cannot draw a graph with no data")
        self.draw_border(draw)
        self.draw_bars(values, draw)
