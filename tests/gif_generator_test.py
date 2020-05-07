from tests.image_testing import compare_gifs, COLORS
from src.gif_strategies.selection_strategies import SelectionSort
from src.gif_strategies.insertion_strategies import InsertionSort
from src.gif_strategies.exchanging_strategies import BubbleSort, CocktailSort, CombSort, OddEvenSort, GnomeSort
from src.gif_strategies.merging_strategies import MergeSort
from src.graph_illustrator import GraphIllustrator
from src.gif_generator import GifStrategy, GifGenerator
from typing import List

OUTPUT_FILEPATH = "./out/images/tests/gif_generator/"
REFERENCE_FILEPATH = "./tests/images/gif_generator/"

def generate_gif_test_helper(file_name: str, strategy: GifStrategy, values: List[int], image_size: (int, int)):
    fp_actual = OUTPUT_FILEPATH + file_name
    fp_expected = REFERENCE_FILEPATH + file_name + ".gif"
    illustrator = GraphIllustrator(len(values), image_size, 10, COLORS)
    gif_generator = GifGenerator(strategy, illustrator)
    gif_generator.generate_gif(values, fp_actual, 1)
    compare_gifs(fp_actual+".gif", fp_expected)

def decreasing(name: str, strategy: GifStrategy):
    file_name = name + "_decreasing"
    values = [230, 207, 184, 161, 138, 115, 92, 69, 46, 23]
    image_size = (250, 250)
    generate_gif_test_helper(file_name, strategy, values, image_size)

def nearly_sorted(name: str, strategy: GifStrategy):
    file_name = name + "_nearly_sorted"
    values = [23, 46, 115, 92, 69, 184, 161, 184, 207, 230]
    image_size = (250, 250)
    generate_gif_test_helper(file_name, strategy, values, image_size)

def few_unique(name: str, strategy: GifStrategy):
    file_name = name + "_few_unique"
    values = [76, 0, 57, 0, 76, 230, 230, 76, 0, 76]
    image_size = (250, 250)
    generate_gif_test_helper(file_name, strategy, values, image_size)

def random(name: str, strategy: GifStrategy):
    file_name = name + "_random"
    values = [84, 191, 151, 194, 216, 43, 28, 67, 61, 86]
    image_size = (250, 250)
    generate_gif_test_helper(file_name, strategy, values, image_size)

class TestSelectionStrategy:
    name ="selection"
    strategy = SelectionSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestBubbleStrategy:
    name = "bubble"
    strategy = BubbleSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestCocktailStrategy:
    name = "cocktail"
    strategy = CocktailSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestCombStrategy:
    name = "comb"
    strategy = CombSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestGnomeStrategy:
    name = "gnome"
    strategy = GnomeSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestOddEvenStrategy:
    name = "odd_even"
    strategy = OddEvenSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestInsertionStrategy:
    name = "insertion"
    strategy = InsertionSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)

class TestMergeStrategy:
    name = "merge"
    strategy = MergeSort()

    def test_decreasing(self):
        decreasing(self.name, self.strategy)

    def test_nearly_sorted(self):
        nearly_sorted(self.name, self.strategy)

    def test_few_unique(self):
        few_unique(self.name, self.strategy)

    def test_random(self):
        random(self.name, self.strategy)
