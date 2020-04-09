from typing import List
from src.gif_strategy import GifStrategy, Step

class MergeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Merge Sort

        TODO: implement
        """
        return NotImplementedError

class InPlaceMergeSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using In-place Merge Sort

        TODO: implement
        """
        return NotImplementedError

class Quadsort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Quadsort

        TODO: implement
        """
        return NotImplementedError