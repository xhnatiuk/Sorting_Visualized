from src.sort_strategy import SortStrategy, Step
from typing import List

class GenerateFrames():

    @property
    def _strategy(self) -> SortStrategy:
        return self._strategy

    def __init__(self, strategy: SortStrategy) -> None:
        """
        Constructor for GenerateFrames class

        Args:
            strategy (SortStrategy): concrete SortStrategy to be used
        """

        self._strategy = strategy

    def generate_steps(self, values: List[int]) -> List[Step]:
        """
        Delegates work to the SortStrategy and returns the steps used in sorting.

        Args:
            values (List[int]): the values to be sorted

        Returns:
            steps (List[Step]): the steps used in sorting
        """
        return self._strategy.sort(values)