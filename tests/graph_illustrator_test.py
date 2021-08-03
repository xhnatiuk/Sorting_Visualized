from src.graph_illustrator import GraphIllustrator
from src.exceptions import InputError
from tests.image_testing import compare_images, COLORS
from typing import List, Tuple
from PIL import Image, ImageDraw

OUTPUT_FILEPATH = "./out/images/tests/graph_illustrator/"
REFERENCE_FILEPATH = "./tests/images/graph_illustrator/"


class TestDrawCursor:

    def helper(self, test_name: str, position: int):
        values = [230, 230, 230, 230, 230]
        size = (250, 250)
        border_width = 50
        fp_actual = OUTPUT_FILEPATH + "cursor/draw_" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "cursor/draw_" + test_name + ".png"
        illustrator = GraphIllustrator(len(values), size, border_width, COLORS)
        graph = Image.new("RGBA", (size[0], size[1]),
                          illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        illustrator.draw_cursor(position, draw, COLORS.cursor)
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "simple"
        self.helper(test_name, 1)

    def test_zero(self):
        test_name = "zero"
        self.helper(test_name, 0)

    def test_maximum(self):
        test_name = "maximum"
        self.helper(test_name, 4)

    def test_negative(self):
        test_name = "negative"
        try:
            self.helper(test_name, -1)
            assert False
        except InputError:
            assert True

    def test_out_of_range(self):
        test_name = "out_of_range"
        try:
            self.helper(test_name, 5)
            assert False
        except InputError:
            assert True


class TestEraseCursor:

    def helper(self, test_name: str, position: int):
        values = [230, 230, 230, 230, 230]
        size = (250, 250)
        border_width = 50
        fp_actual = OUTPUT_FILEPATH + "cursor/erase_" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "cursor/erased" + ".png"
        illustrator = GraphIllustrator(len(values), size, border_width, COLORS)
        graph = Image.new("RGBA", (size[0], size[1]),
                          illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        # erase first to check erase_cursor handling
        illustrator.erase_cursor(position, draw)
        # then draw and erase to make sure it is actually eraseing!
        illustrator.draw_cursor(position, draw, COLORS.cursor)
        illustrator.erase_cursor(position, draw)
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "simple"
        self.helper(test_name, 1)

    def test_zero(self):
        test_name = "zero"
        self.helper(test_name, 0)

    def test_maximum(self):
        test_name = "maximum"
        self.helper(test_name, 4)

    def test_negative(self):
        test_name = "negative"
        try:
            self.helper(test_name, -1)
            assert False
        except InputError:
            assert True

    def test_out_of_range(self):
        test_name = "out_of_range"
        try:
            self.helper(test_name, 5)
            assert False
        except InputError:
            assert True


class TestDrawBar:

    def helper(self, test_name: str, position: int, value: int):
        values = [230, 230, 230, 230, 230, 230, 230, 230, 230, 230]
        size = (250, 250)
        border_width = 10
        fp_actual = OUTPUT_FILEPATH + "bar/draw_" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "bar/draw_" + test_name + ".png"
        illustrator = GraphIllustrator(len(values), size, border_width, COLORS)
        graph = Image.new("RGBA", (size[0], size[1]),
                          illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        illustrator.draw_bar(position, value, draw, COLORS.bar)
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "simple"
        self.helper(test_name, 5, 200)

    def test_zero(self):
        test_name = "zero"
        self.helper(test_name, 0, 200)

    def test_maximum(self):
        test_name = "maximum"
        self.helper(test_name, 9, 200)

    def test_negative(self):
        test_name = "negative"
        try:
            self.helper(test_name, -1, 200)
            assert False
        except InputError:
            assert True

    def test_out_of_range(self):
        test_name = "out_of_range"
        try:
            self.helper(test_name, 10, 200)
            assert False
        except InputError:
            assert True

    def test_value_zero(self):
        test_name = "value_zero"
        self.helper(test_name, 5, 0)

    def test_value_negative(self):
        test_name = "value_negative"
        try:
            self.helper(test_name, 5, -1)
            assert False
        except InputError:
            assert True


class TestEraseBar:

    def helper(self, test_name: str, position: int):
        values = [230, 230, 230, 230, 230, 230, 230, 230, 230, 230]
        size = (250, 250)
        border_width = 10
        fp_actual = OUTPUT_FILEPATH + "bar/erase_" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "bar/erased" + ".png"
        illustrator = GraphIllustrator(len(values), size, border_width, COLORS)
        graph = Image.new("RGBA", (size[0], size[1]),
                          illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        # erase first to check erase_cursor handling
        illustrator.erase_bar(position, draw)
        # then draw and erase to make sure it is actually eraseing!
        illustrator.draw_bar(position, 200, draw, COLORS.bar)
        illustrator.erase_bar(position, draw)
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "pos_simple"
        self.helper(test_name, 5)

    def test_zero(self):
        test_name = "pos_zero"
        self.helper(test_name, 0)

    def test_maximum(self):
        test_name = "pos_maximum"
        self.helper(test_name, 9)

    def test_negative(self):
        test_name = "pos_negative"
        try:
            self.helper(test_name, -1)
            assert False
        except InputError:
            assert True

    def test_out_of_range(self):
        test_name = "pos_out_of_range"
        try:
            self.helper(test_name, 10)
            assert False
        except InputError:
            assert True


class TestDrawBars:

    def helper(self, test_name: str, values: List[int]):
        size = (250, 250)
        border_width = 10
        fp_actual = OUTPUT_FILEPATH + "bar/bars_" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "bar/bars_" + test_name + ".png"
        illustrator = GraphIllustrator(len(values), size, border_width, COLORS)
        graph = Image.new("RGBA", (size[0], size[1]),
                          illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        illustrator.draw_bars(
            values,
            draw,
        )
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "simple"
        values = [100, 100, 100]
        self.helper(test_name, values)

    def test_empty(self):
        test_name = "empty"
        values = []
        self.helper(test_name, values)

    def test_negative(self):
        test_name = "negative"
        values = [100, -5, 100]
        try:
            self.helper(test_name, values)
            assert False
        except InputError:
            assert True


class TestDrawBorder:

    def helper(self, test_name: str, size: Tuple[int, int], border_width: int):
        values = [1]
        fp_actual = OUTPUT_FILEPATH + "border/" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "border/" + test_name + ".png"
        illustrator = GraphIllustrator(len(values), size, border_width, COLORS)
        graph = Image.new("RGBA", (size[0], size[1]),
                          illustrator.colors.background)
        draw = ImageDraw.Draw(graph)
        illustrator.draw_border(draw)
        graph.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "simple"
        size = (250, 250)
        border_width = 10
        self.helper(test_name, size, border_width)

    def test_zero(self):
        test_name = "zero"
        size = (250, 250)
        border_width = 0
        self.helper(test_name, size, border_width)

    def test_maximum(self):
        test_name = "maximum"
        size = (250, 250)
        border_width = 250
        self.helper(test_name, size, border_width)

    def test_negative(self):
        test_name = "negative"
        size = (250, 250)
        border_width = -1
        try:
            self.helper(test_name, size, border_width)
            assert False
        except InputError:
            assert True

    def test_out_of_range(self):
        test_name = "out_of_range"
        size = (250, 250)
        border_width = 251
        try:
            self.helper(test_name, size, border_width)
            assert False
        except InputError:
            assert True


class TestDrawGraph:

    def draw_graph_test_helper(self, file_name: str, values: List[int],
                               image_size: Tuple[int, int]):
        fp_actual = OUTPUT_FILEPATH + "graph/" + file_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "graph/" + file_name + ".png"
        illustrator = GraphIllustrator(len(values), image_size, 10, COLORS)
        graph = Image.new("RGBA", (image_size[0], image_size[1]),
                          illustrator.colors.background)
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

    def test_size(self):
        file_name = "size_small"
        values = [230, 230, 230, 230, 230, 230, 230, 230, 230, 230]
        image_size = (250, 250)
        self.draw_graph_test_helper(file_name, values, image_size)

    def test_size_medium(self):
        file_name = "size_medium"
        values = [
            480,
            480,
            480,
            480,
            480,
            480,
            480,
            480,
            480,
            480,
        ]
        image_size = (500, 500)
        self.draw_graph_test_helper(file_name, values, image_size)

    def test_size_large(self):
        file_name = "size_large"
        values = [730, 730, 730, 730, 730, 730, 730, 730, 730, 730]
        image_size = (750, 750)
        self.draw_graph_test_helper(file_name, values, image_size)
