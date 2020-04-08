from typing import List
from src.sort_strategy import FrameStrategy, Step

class Introsort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Introsort

        TODO: implement
        """
        return NotImplementedError

class Quicksort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Quicksort

        TODO: implement
        """
        return NotImplementedError

class Quicksort3(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Quicksort3

        TODO: implement
        """
        return NotImplementedError
