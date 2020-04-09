from src.gif_strategy import GifStrategy, Step
from src.graph_illustrator import GraphIllustrator
from typing import List
from copy import copy, deepcopy
from PIL import Image, ImageDraw

class GifGenerator():
    def __init__(self, strategy: GifStrategy, illustrator = GraphIllustrator) -> None:
        """
        Constructor for GifGenerator class

        Args:
            strategy (GifStrategy): concrete GifStrategy to be used

        """
        self.illustrator = illustrator
        self._strategy = strategy
      
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Delegates work to the GifStrategy and returns the steps used in sorting.

        Args:
            values (List[int]): the values to be sorted

        Returns:
            steps (List[Step]): the steps used in sorting
        """
        sorting_list = values.copy()
        return self._strategy.generate_steps(sorting_list)

    def generate_gif(self, values: List[int], file_path: str) -> int:
        """
        generates images of the graph coresponding to the changes in steps

        Args:
            values (List[int]): the list of values displayed in each frame
            steps (Step): a list corresponding to the frames to be generated
            graph (Image): the starting image
        
        Modifies:
            values: sorts the list in increasing order
            ./file_path : save a gif

        Returns:
            None
        """
        steps = self.generate_steps(values)
        graph = Image.open(file_path)
        if file_path[0] == ".":
            file_path = file_path[2:]
        file_path = file_path[:file_path.find('.')]
        file_path = file_path + ".gif"
        frames = []
        gif = graph.copy()
        steps = self.generate_steps(values)
        last_frame = graph
        for step in steps:
            frame = last_frame.copy()
            self.generate_frame(values, step, frame)
            frames.append(frame)
            last_frame = frame.copy()
            draw = ImageDraw.Draw(last_frame)
            self.illustrator.erase_cursor(step.position, draw)
        gif.save(file_path, save_all=True, append_images=frames)

    def generate_frame(self, values: List[int], step: Step, frame: Image) -> None:
        """
        edits the image to display the changes in Step, performs any swaps on values

        Args:
            values (List[int]): the list of values displayed in frame
            step (Step): the new position for the cursor and possibly a swap of bars
            frame (Image): the image to be edited

        Modifies:
            frame : updated with the changes in step
            values: possibly swaps two of the values positions

        Returns: 
            None
        """
        draw = ImageDraw.Draw(frame)
        self.illustrator.draw_cursor(step.position, draw, self.illustrator.colors.cursor)
        if step.swap != None:
            index_1 = step.swap[0]
            index_2 = step.swap[1]
            value_1 = values[index_1]
            value_2 = values[index_2]
            self.illustrator.erase_bar(index_1, draw)
            self.illustrator.erase_bar(index_2, draw)
            self.illustrator.draw_bar(index_1, value_2, draw, self.illustrator.colors.bar)
            self.illustrator.draw_bar(index_2, value_1, draw, self.illustrator.colors.bar)
            values[index_1] = value_2
            values[index_2] = value_1
            