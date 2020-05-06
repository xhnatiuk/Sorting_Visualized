from abc import ABC, abstractmethod
from .graph_illustrator import GraphIllustrator
from typing import List
from copy import copy
from PIL import Image, ImageDraw

class GifStrategy(ABC):
    """
    Interface that declares contract for concrete gif strategy classes.
    """

    @abstractmethod
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Sorts the values and returns a list of the steps used.
        
        Args:
            values (List[int]): the values to be sorted.

        Modifies:
            values: sorts the list in increasing order.
            
        Returns:
            steps(List[Step]): the list of steps used.
        """
        pass

class Step:
    """
    Object for tracking steps taken while sorting a list.

    Attributes:
        position (int): the index of the value being considered in the current step.
        changes (List[Change]): a list of 0 or more changes applied in the current step.
    """
    position: int
    changes: List[Change]

    def __init__(self, position: int, changes: List[Change] = None):
        """
        Constructor for Step class.

        Args:
            position (int): the index of the value being considered.
            changes (List[Change]): a list of 0 or more changes applied.
        """
        self.position = position
        self.changes = changes 

class Change:
    """
    Class for defining changes that have taken place during sorting. 

    Attributes: 
        indentifier (str): the indentifier of a change. Identifiers: 
                draw - a value at a single index was changed.
                overlay - a value at a single index will be changed.
                exchange - values at two different indicies were swapped.
                add_cursor - values were considered at 1 or more indicies.
                remove_cursor - values were no longer being considered at 1 or more indicies.
                color - values were re-colored at 0 or more indicies.
            involved (List[int]): values involved in a change. See GifGenerator.apply_<indentifier>
                for information on how the invovled list should be used for each identifier.
    """
    indentifier: str
    involved: List[int]

    def __init__(self, indentifier: str, involved: List[int]):
        """
        Constructor for Change class.

        Args:
            identifier (str): the indentifier of the change applied.
            involved (List[int]): values involved in the change. 
            
        """
        self.indentifier = indentifier
        self.involved = involved 

class GifGenerator():
    """
    Object containing a GifStrategy and a GrahIllustrator for GIF file generation

    Attributes:
        illustrator (GraphIllustrator): GraphIllustrator used for frame drawing.
        strategy (GifStrategy): GifStrategy to be used for step generation.
    """
    def __init__(self, strategy: GifStrategy, illustrator = GraphIllustrator) -> None:
        """
        Constructor for GifGenerator class.

        Args:
            strategy (GifStrategy): concrete GifStrategy to be used.
            illustrator (GraphIllustrator): concrete GraphIllustrator to be used.
        """
        self.illustrator = illustrator
        self.strategy = strategy
      
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Delegates work to the GifStrategy and returns the steps used in sorting.

        Args:
            values (List[int]): the values to be sorted.

        Returns:
            steps (List[Step]): the steps used in sorting.
        """
        sorting_list = values.copy()
        return self.strategy.generate_steps(sorting_list)

    def generate_gif(self, values: List[int], file_path: str, speed: int) -> None:
        """
        Generates a GIF with frames corresponding to the steps taken by the GifGenerator's sorting strategy.

        Args:
            values (List[int]): the list of values in the bar graph.
            file_path (str): the location where the png that the gif will be based off of is stored,
                and where the gif willl be stored.
            speed (int): the duration of each frame in centiseconds.
        
        Modifies:
            values: sorts the list in increasing order.
            ./file_path: save a gif.

        Returns:
            None.
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
        Edits the frame to display the changes in Step, performs any changes on values.

        Args:
            values (List[int]): the list of values displayed in frame.
            step (Step): the new position for the cursor and 0 or more changes.
            frame (Image): the image to be edited.

        Modifies:
            frame: updated with the changes in step.
            values: values may be changed or moved.

        Returns: 
            None.
        """
        draw = ImageDraw.Draw(frame)
        self.illustrator.draw_cursor(step.position, draw, self.illustrator.colors.cursor)
        if step.changes:
            for change in step.changes:
                self.change_dispatch(change, values, draw)

    def change_dispatch(self, change: Change, values:List[int], draw: ImageDraw) -> None:
        """
        Calls the appropriate function for the given change code.

        Args:
            change (Change): object containing the change identifier and involved values.
            values (List[int]): the list of values displayed in frame.
            draw (ImageDraw): the drawing object.

        Modifies:
            values: values may be changed or moved.
            draw: the image associated with the drawing object is updated with the appropriate changes.

        Returns:
            None.
        """
        method_name = "apply_" + str(change.indentifier)
        method = getattr(self, method_name)
        return method(values, change.invovled, draw)
    
    def apply_draw(self, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        """
        Draws a bar on the image at involved[0] with value involved[1], updates values accordingly. 

        Args:
            values (List[int]): the list of values displayed in frame.
            involved (List[int]): the index and value for the bar to be drawn.
            draw (ImageDraw): the drawing object.

        Modifies:
            values: the value at index involved[0] is set to involved[1].
            draw: the bar at index involved[0] is erased and replaced with a bar of value involved[1] on image associated with the drawing object.

        Returns:
            None.
        """
        index = involved[0]
        value = involved[1]
        print(index)
        self.illustrator.erase_bar(index, draw)
        self.illustrator.draw_bar(index, value, draw, self.illustrator.colors.bar)
        values[index] = value

    def apply_overlay(self, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        """
        Draws a bar-outline on the image at involved[0] with value involved[1], updates values accordingly. 

        Args:
            values (List[int]): the list of values displayed in frame.
            involved (List[int]): the index and value for the bar-outline to be drawn.
            draw (ImageDraw): the drawing object.

        Modifies:
            values: the value at index involved[0] is set to involved[1].
            draw: a bar outline with value involved[1] is drawn over top of the bar at index involved[0] on image associated with the drawing object.

        Returns:
            None.
        """
        index = involved[0]
        value = involved[1]
        self.illustrator.draw_bar_outline(index, value, draw, self.illustrator.colors.finished)
        values[index] = value
                    
    def apply_exchange(self, values: List[int], involved: List[int], draw: ImageDraw) -> None:
        """
        Swaps the bars on the image at involved[0] and involved[1], updates values accordingly. 

        Args:
            values (List[int]): the list of values displayed in frame.
            involved (List[int]): the indicies of the bars to be swapped.
            draw (ImageDraw): the drawing object.

        Modifies:
            values: the value at index involved[0] is swapped with the value at index invovled[1].
            draw: the bars at index involved[0]  and involved[1] are swapped on image associated with the drawing object.

        Returns:
            None.
        """
        index_1 = involved[0]
        index_2 = involved[1]
        value_1 = values[index_1]
        value_2 = values[index_2]
        self.apply_draw(values, [index_1, value_2], draw)
        self.apply_draw(values, [index_2, value_1], draw)

    def apply_add_cursor(self, values: List[int], involved: List[int], draw: ImageDraw) -> None:
        """
        Draws a cursor on the image at every index listed in involved. 

        Args:
            values (List[int]): the list of values displayed in frame.
            involved (List[int]): the indicies of the cursors to be drawn.
            draw (ImageDraw): the drawing object.

        Modifies:
            draw: cursors are drawn on image associated with the drawing object at every index listed in involved.

        Returns:
            None.
        """
        for i in involved:
                self.illustrator.draw_cursor(i, draw, self.illustrator.colors.cursor)

    def apply_remove_cursor(self, values: List[int], involved: List[int], draw: ImageDraw) -> None:
        """
        Erases a cursor on the image at every index listed in involved. 

        Args:
            values (List[int]): the list of values displayed in frame.
            involved (List[int]): the indicies of the cursors to be erased.
            draw (ImageDraw): the drawing object.

        Modifies:
            draw: cursors are erased on image associated with the drawing object at every index listed in involved.

        Returns:
            None.
        """
        for i in involved:
            self.illustrator.erase_cursor(i, draw)

    def apply_color(self, values:List[int], involved: List[int], draw: ImageDraw) -> None:
        """
        Re-draws all bars at indicies in involved[1:] on the image with the color specified in involved[0]. 

        Args:
            values (List[int]): the list of values displayed in frame.
            involved (List[int]): the color code and indicies of re-coloring bars.
            draw (ImageDraw): the drawing object.

        Modifies:
            draw:  all bars at indicies in involved[1:] are erased and re-drawn with the selected color on image associated with the drawing object.

        Returns:
            None.
        """
        color = self.select_color(involved[0])
        involved = involved[1:]
        for index in involved:
            self.illustrator.erase_bar(index, draw)
            self.illustrator.draw_bar(index, values[index], draw, color)

    def select_color(self, code: str) -> (int, int, int):
        """
        Selects the correct color from the GraphIllustrator's ColorProfile based on the code.

        Args:
            code (str): one of the color options (sorted, fade, or bar).

        Returns:
            color (int, int, int): a RGBA color code.
        """
        switcher = {
            "sorted": self.illustrator.colors.finished,
            "fade": self.illustrator.colors.fade,
            "bar": self.illustrator.colors.bar,
        }
        return switcher.get(code, None) 