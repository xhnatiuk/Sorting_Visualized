from typing import List
from src.gif_strategy import GifStrategy, Step

class PatienceSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Patience Sort

        TODO: implement
        """
        return NotImplementedError

class BlockSort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Block Sort

        TODO: implement
        """
        return NotImplementedError

class Timsort(GifStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the GifStrategy.generate_steps contract using Timsort

        TODO: implement
        """
        return NotImplementedError