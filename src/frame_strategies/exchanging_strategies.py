from typing import List
from src.sort_strategy import FrameStrategy, Step

class BubbleSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Bubble Sort

        TODO: implement
        """
        return NotImplementedError

class CocktailSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Cocktail Sort

        TODO: implement
        """
        return NotImplementedError

class CombSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Comb Sort

        TODO: implement
        """
        return NotImplementedError

class GnomeSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Gnome Sort

        TODO: implement
        """
        return NotImplementedError

class OddEvenSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Odd-Even Sort

        TODO: implement
        """
        return NotImplementedError