from typing import List
from src.sort_strategy import FrameStrategy, Step

class MergeSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Merge Sort

        TODO: implement
        """
        return NotImplementedError

class InPlaceMergeSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using In-place Merge Sort

        TODO: implement
        """
        return NotImplementedError

class Quadsort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Quadsort

        TODO: implement
        """
        return NotImplementedError