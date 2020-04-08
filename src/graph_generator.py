from typing import List
from PIL import Image, ImageDraw
from src.graph_strategy import GraphStrategy
from src.illustrator import Illustrator
from src.exceptions import InputError

class GraphGenerator():
    def __init__(self, strategy: GraphStrategy) -> None:

        """
        Constructor for GraphGenerator class

        Args:
            strategy (GraphStrategy): an instance of a concrete GraphStrategy
        """
        self._strategy = strategy
     

    def generate_graph(self, quantity: int, illustrator: Illustrator, file_path: str) -> None:
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
            None
        """
        maximum_value = illustrator.image_height - 2*illustrator.border_size
        if quantity < 1:
            raise InputError(quantity, "cannot generate graph with less than 1 value")
        if maximum_value < 0:
            raise InputError(maximum_value, "cannot generate a graph with negative values")
        values = self._strategy.generate_values(quantity, maximum_value)
        graph = self.create_graph_base(illustrator.image_width, illustrator.image_height, illustrator.background_color)
        draw = ImageDraw.Draw(graph)
        graph = illustrator.draw_graph(values, draw)
        fp = "./out/"+file_path+".png"
        graph.save(fp)

    def create_graph_base(self, width: (int), height: (int), background_color: (int, int, int, int)) -> Image:
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
        if (width, height) < (1, 1):
            raise InputError((width, height), "image size cannot be less than 1")
        return Image.new("RGBA", (width, height), background_color)
        