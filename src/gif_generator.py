from .gif_strategy import GifStrategy, Step, Change
from .graph_illustrator import GraphIllustrator
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

    def generate_gif(self, values: List[int], file_path: str, speed: int) -> None:
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
        base_img_path = file_path + ".png"
        graph = Image.open(base_img_path)
        if file_path[0] == ".":
            file_path = file_path[2:]
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
        gif.save(file_path, save_all=True, append_images=frames, duration=speed*10)

    def generate_frame(self, values: List[int], step: Step, frame: Image) -> None:
        """
        edits the image to display the changes in Step, performs any changes on values

        Args:
            values (List[int]): the list of values displayed in frame
            step (Step): the new position for the cursor and cahnges (if any)
            frame (Image): the image to be edited

        Modifies:
            frame : updated with the changes in step
            values: possibly swaps two of the values positions

        Returns: 
            None
        """
        draw = ImageDraw.Draw(frame)
        self.illustrator.draw_cursor(step.position, draw, self.illustrator.colors.cursor)
        if step.changes:
            for change in step.changes:
                self.step_dispatch(change.type, values, change.involved, draw)

    def step_dispatch(self, code: str, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        method_name = "apply_" + str(code)
        method = getattr(self, method_name)
        return method(values, involved, draw)
    
    def apply_draw(self, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        index = involved[0]
        value = involved[1]
        print(index)
        self.illustrator.erase_bar(index, draw)
        self.illustrator.draw_bar(index, value, draw, self.illustrator.colors.bar)
        values[index] = value

    def apply_overlay(self, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        index = involved[0]
        value = involved[1]
        self.illustrator.draw_bar_outline(index, value, draw, self.illustrator.colors.finished)
        values[index] = value
                    
    def apply_exchange(self, values: List[int], involved: List[int], draw: ImageDraw) -> None:
        index_1 = involved[0]
        index_2 = involved[1]
        value_1 = values[index_1]
        value_2 = values[index_2]
        self.apply_draw(values, [index_1, value_2], draw)
        self.apply_draw(values, [index_2, value_1], draw)

    def apply_add_cursor(self, values: List[int], involved: List[int], draw: ImageDraw) -> None:
        for i in involved:
                self.illustrator.draw_cursor(i, draw, self.illustrator.colors.cursor)

    def apply_remove_cursor(self, values: List[int], involved: List[int], draw: ImageDraw) -> None:
        for i in involved:
            self.illustrator.erase_cursor(i, draw)

    def apply_color(self, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        color = self.select_color(involved[0])
        involved = involved[1:]
        for index in involved:
            self.illustrator.erase_bar(index, draw)
            self.illustrator.draw_bar(index, values[index], draw, color)

    def select_color(self, code: str) -> (int, int, int, int):
        """
        Selects the correct color based on the code

        Args:
            code (string): one of the preset color options

        Returns:
            color (int, int, int, int): a RGBA color code
        """
        switcher = {
            "sorted": self.illustrator.colors.finished,
            "fade": self.illustrator.colors.fade,
            "bar": self.illustrator.colors.bar,
        }
        return switcher.get(code, None) 