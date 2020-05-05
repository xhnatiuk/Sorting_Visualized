from typing import List
from PIL import Image, ImageDraw
from .graph_strategy import GraphStrategy
from .graph_illustrator import GraphIllustrator
from .exceptions import InputError

class GraphGenerator():
    def __init__(self, strategy: GraphStrategy) -> None:

        """
        Constructor for GraphGenerator class

        Args:
            strategy (GraphStrategy): an instance of a concrete GraphStrategy
        """
        self._strategy = strategy
     

    def generate_graph(self, quantity: int, illustrator: GraphIllustrator, file_path: str) -> List[int]:
        """
        generates and saves an image of a graph
        
        Args:
            quantity (int): the number of bars on the graph
            illustrator (Illustrator): the illistrator instance for the graph generation
            file_path (string): the path relative to ./out to save the graph to

        Modifies
            ./out

        Raises:
            InputError: 
                *less than 1 value
                *negative maximum value
                *illustrator image size less than 1
                *number of values is too large for the image size

        Returns:
            values (List[int]): the values used in the generated graph
        """
        if quantity < 1:
            raise InputError(quantity, "cannot generate graph with less than 1 value")
        maximum_value = illustrator.image_height - 2*illustrator.border_size
        if maximum_value < 0:
            raise InputError(maximum_value, "cannot generate a graph with negative values")
        values = self._strategy.generate_values(quantity, maximum_value)
        graph = create_graph_base(illustrator.image_width, illustrator.image_height, illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        illustrator.draw_graph(values, draw)
        fp = file_path+".png"
        graph.save(fp)
        return values

def create_graph_base(width: (int), height: (int), background_color: (int, int, int, int)) -> Image:
    """
    creates a base image to draw a graph on
    
    Args:
        width (int): the width of the image in pixels
        height (int): the width of the image in pixels
        background_color (string): the RGBA color code for the background

    Raises:
        InputError: image size less than 1

    Returns:
        base (Image): the base for the graph
    """
    if width < 1 or height < 1:
        raise InputError((width, height), "image size cannot be less than 1")
    return Image.new("RGBA", (width, height), background_color)
        