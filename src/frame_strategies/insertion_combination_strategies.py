from typing import List
from src.sort_strategy import FrameStrategy, Step

class PatienceSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Patience Sort

        TODO: implement
        """
        return NotImplementedError

class BlockSort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Block Sort

        TODO: implement
        """
        return NotImplementedError

class Timsort(FrameStrategy):
    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Fufuills the FrameStrategy.generate_steps contract using Timsort

        TODO: implement
        """
        return NotImplementedError