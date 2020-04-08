from src.graph_illustrator import GraphIllustrator, ColorProfile
from src.graph_generator import GraphGenerator
from src.graph_strategy import GraphStrategy
from src.exceptions import InputError
from tests.image_testing import assert_image_equal
from typing import List
from PIL import Image, ImageDraw

OUTPUT_FILEPATH = "./out/images/tests/graph_illustrator/"
REFERENCE_FILEPATH = "./tests/images/graph_illustrator/"

COLORS = ColorProfile((255, 255, 255, 255), (0, 0, 0, 255), (33, 150, 243, 255), (243, 33, 45, 255), (243, 33, 45, 255))

def compare_images(fp_actual: str, fp_expected: str):
    actual = Image.open(fp_actual)
    expected = Image.open(fp_expected)
    assert_image_equal(actual, expected)

class MockGraphStrategy(GraphStrategy):
    def generate_values(self, quantity: int, maximum: int) -> List[int]:
        return []

class TestDrawGraph:
   


        
    def draw_graph_test_helper(self, file_name: str, values: List[int], image_size: (int, int)):
        fp_actual = OUTPUT_FILEPATH + "draw_graph/" + file_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "draw_graph/" + file_name + ".png"
        illustrator = GraphIllustrator(len(values), image_size, 10, COLORS)
        graph_generator = GraphGenerator(MockGraphStrategy())
        graph =  graph_generator.create_graph_base(image_size[0], image_size[1], (255, 255, 255, 255))
        draw = ImageDraw.Draw(graph)
        illustrator.draw_graph(values, draw)
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_values_one(self):
        file_name = "values_one"
        values = [50]
        image_size = (100, 100)
        self.draw_graph_test_helper(file_name, values, image_size)

    def test_values_none(self):
        file_name = "values_none"
        values = []
        image_size = (100, 100)
        try:
            self.draw_graph_test_helper(file_name, values, image_size)
            assert False
        except InputError:
            assert True
    
    def test_values_too_many(self):
        file_name = "values_too_many"
        values = [1, 2, 3, 4, 5, 6]
        image_size = (30, 30)
        try:
            self.draw_graph_test_helper(file_name, values, image_size)
            assert False
        except InputError:
            assert True


    def test_size_zero(self):
        file_name = "size_zero"
        values = [0, 1, 2, 3, 4, 5]
        image_size = (0, 0)
        try: 
            self.draw_graph_test_helper(file_name, values, image_size)
            assert False
        except InputError:
            assert True

    def test_size_small(self):
        file_name = "size_small"
        values = [230, 230, 230, 230, 230, 230, 230, 230, 230, 230]
        image_size = (250, 250)
        self.draw_graph_test_helper(file_name, values, image_size)

    def test_size_medium(self):
        file_name = "size_medium"
        values = [480, 480,  480, 480, 480, 480, 480, 480, 480, 480,]
        image_size = (500, 500)
        self.draw_graph_test_helper(file_name, values, image_size)

    def test_size_large(self):
        file_name = "size_large"
        values = [730, 730, 730, 730, 730, 730, 730, 730, 730, 730]
        image_size = (750, 750)
        self.draw_graph_test_helper(file_name, values, image_size)


def test_draw_cursor():
    test_name = "draw_cursor_position_zero"
    fp_actual = OUTPUT_FILEPATH + test_name + ".png"
    fp_expected = REFERENCE_FILEPATH + test_name + ".png"
    values = [230, 230, 230, 230, 230, 230, 230, 230, 230, 230]
    image_size = (250, 250)
    illustrator = GraphIllustrator(len(values), image_size, 10, COLORS)
    graph_generator = GraphGenerator(MockGraphStrategy())
    graph =  graph_generator.create_graph_base(image_size[0], image_size[1], (255, 255, 255, 255))
    draw = ImageDraw.Draw(graph)
    illustrator.draw_graph(values, draw)
    illustrator.draw_cursor(0, draw, COLORS.cursor)
    graph.save(fp_actual)
    compare_images(fp_actual, fp_expected)