from tests.image_testing import compare_images, COLORS
from src.gif_strategies.selection_strategies import SelectionSort
from src.graph_illustrator import GraphIllustrator
from src.gif_generator import GifGenerator
from src.gif_strategy import GifStrategy
from typing import List

OUTPUT_FILEPATH = "./out/images/tests/gif_generator/"
REFERENCE_FILEPATH = "./tests/images/gif_generator/"


def generate_gif_test_helper(file_name: str, strategy: GifStrategy, values: List[int], image_size: (int, int)):
    fp_actual = OUTPUT_FILEPATH + file_name
    fp_expected = REFERENCE_FILEPATH + file_name + ".gif"
    illustrator = GraphIllustrator(len(values), image_size, 10, COLORS)
    gif_generator = GifGenerator(strategy, illustrator)
    gif_generator.generate_gif(values, fp_actual+".png")
    compare_images(fp_actual+".gif", fp_expected)

def test_selection_strategy_small():
    file_name = "selection_small"
    values = [230, 220, 200, 170, 150, 130, 100, 80, 50, 30]
    image_size = (250, 250)
    strategy = SelectionSort()
    generate_gif_test_helper(file_name, strategy, values, image_size)
    