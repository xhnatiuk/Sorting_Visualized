from src.frame_strategy import FrameStrategy, Step
from typing import List
from copy import copy
from PIL import Image, ImageDraw

class FrameGenerator():
    def __init__(self, strategy: FrameStrategy, ) -> None:
        """
        Constructor for FrameGenerator class

        Args:
            strategy (FrameStrategy): concrete FrameStrategy to be used

        """
        self._strategy = strategy
      
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Delegates work to the FrameStrategy and returns the steps used in sorting.

        Args:
            values (List[int]): the values to be sorted

        Returns:
            steps (List[Step]): the steps used in sorting
        """
        sorting_list = values.copy()
        return self._strategy.sort(sorting_list)

    def generate_frames(self, values: List[int], steps: List[Step], file_path: str) -> int:
        """
        generates images of the graph coresponding to the changes in steps

        Args:
            values (List[int]): the list of values displayed in frame
            steps (Step): a list corresponding to the frames to be generated
            graph (Image): the starting image
        
        Modifies:
            values: sorts the list in increasing order

        Returns:
            num_frames (int): the number of frames generated
        """
        graph = Image.open(file_path)
        fp = copy.copy(file_path)
        fp = fp[:fp.find('.')]
        num_frames = 0
        graph.save(fp+num_frames+".png")
        steps = self.generate_steps(values)
        for step in steps:            
            self.draw_frame(values, step, graph)
            num_frames = num_frames + 1
            graph.save(fp + num_frames +".png")
            self.draw_cursor(step.position, graph, self._background_color)
        return num_frames + 1

    def create_frame(self, values: List[int], step: Step, frame: Image) -> None:
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


    def replace_bar(self) -> None:
        """
        swaps two bars
        """