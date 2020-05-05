from src.graph_generator import *
from src.graph_strategy import *
from src.graph_illustrator import GraphIllustrator
from tests.image_testing import compare_images, COLORS

OUTPUT_FILEPATH = "./out/images/tests/graph_generator/"
REFERENCE_FILEPATH = "./tests/images/graph_generator/"

class TestCreateGraphBase:
    def helper(self, test_name: str, width: int, height: int):
        fp_actual = OUTPUT_FILEPATH + "base_" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "base_" + test_name + ".png"
        base = create_graph_base(width, height, COLORS.background)
        base.save(fp_actual)
        compare_images(fp_actual, fp_expected)

    def test_simple(self):
        test_name = "simple"
        self.helper(test_name, 1, 1)

    def test_width_zero(self):
        test_name = "width_zero"
        try:
            self.helper(test_name, 0, 10)
            assert False
        except InputError:
            assert True

    def test_height_zero(self):
        test_name = "height_zero"
        try:
            self.helper(test_name, 10, 0)
            assert False
        except InputError:
            assert True

class MockEmptyStrategy(GraphStrategy):
    def generate_values(self, quantity, maximum):
        return []

class MockSimpleStrategy(GraphStrategy):
    def generate_values(self, quantity, maximum):
        output = []
        for i in range(quantity):
            output.append(maximum)
        return output

class TestGenerateGraph:
    simple_quantity = 10
    simple_illustrator = GraphIllustrator(simple_quantity, (250, 250), 10, COLORS)

    def helper(self, test_name: str, quantity: int, strategy: GraphStrategy, 
    illustrator: GraphIllustrator):
        fp_actual = OUTPUT_FILEPATH + "" + test_name + ".png"
        fp_expected = REFERENCE_FILEPATH + "" + test_name + ".png"
        fp_function = OUTPUT_FILEPATH + test_name
        generator = GraphGenerator(strategy)
        generator.generate_graph(quantity, illustrator, fp_function)
        compare_images(fp_actual, fp_expected)
    
    # for tests that will have different outputs depending on random seed
    def helper_no_compare(self, test_name: str, quantity: int, strategy: GraphStrategy, 
    illustrator: GraphIllustrator):
        fp_function = OUTPUT_FILEPATH + test_name
        generator = GraphGenerator(strategy)
        generator.generate_graph(quantity, illustrator, fp_function)
        assert True

    def test_increasing(self):
        test_name = "increasing"
        quantity = self.simple_quantity
        strategy = Increasing()
        illustrator = self.simple_illustrator
        self.helper(test_name, quantity, strategy, illustrator)

    def test_decreasing(self):
        test_name = "decreasing"
        quantity = self.simple_quantity
        strategy = Decreasing()
        illustrator = self.simple_illustrator
        self.helper(test_name, quantity, strategy, illustrator)
    
    def test_nearly_sorted(self):
        test_name =  "nearly_sorted"
        quantity = self.simple_quantity
        strategy = NearlySorted()
        illustrator = self.simple_illustrator
        self.helper_no_compare(test_name, quantity, strategy, illustrator)
    
    def test_few_unique(self):
        test_name = "few_unique"
        quantity = self.simple_quantity
        strategy = FewUnique()
        illustrator = self.simple_illustrator
        self.helper_no_compare(test_name, quantity, strategy, illustrator)

    def test_random(self):
        test_name = "random"
        quantity = self.simple_quantity
        strategy = Random()
        illustrator = self.simple_illustrator
        self.helper_no_compare(test_name, quantity, strategy, illustrator)
    
    def test_empty(self):
        test_name = "mock_empty"
        quantity = self.simple_quantity
        strategy = MockEmptyStrategy()
        illustrator = self.simple_illustrator
        try: 
            self.helper(test_name, quantity, strategy, illustrator)
            assert False
        except InputError:
            assert True

    def test_quantity_one(self):
        test_name = "quantity_one"
        quantity = 1
        strategy = MockSimpleStrategy()
        illustrator = GraphIllustrator(quantity, (250, 250), 10, COLORS)
        self.helper(test_name, quantity, strategy, illustrator)

    def test_quantity_zero(self):
        test_name = "quantity_zero"
        quantity = 0
        strategy = MockSimpleStrategy()
        illustrator = self.simple_illustrator
        try: 
            self.helper(test_name, quantity, strategy, illustrator)
            assert False
        except InputError:
            assert True

    def test_maximum_zero(self):
        test_name = "maximum_zero"
        quantity = self.simple_quantity
        strategy = Increasing()
        illustrator = GraphIllustrator(quantity, (250, 100), 50, COLORS)
        self.helper(test_name, quantity, strategy, illustrator)

    def test_maximum_negative(self):
        test_name = "maximum_negative"
        quantity = self.simple_quantity
        strategy = MockEmptyStrategy()
        illustrator = GraphIllustrator(quantity, (250, 250), 126, COLORS)
        try: 
            self.helper(test_name, quantity, strategy, illustrator)
            assert False
        except InputError:
            assert True

    def test_width_one(self):
        test_name = "width_one"
        quantity = self.simple_quantity
        strategy = Increasing()
        illustrator = GraphIllustrator(quantity, (59, 100), 20, COLORS)
        self.helper(test_name, quantity, strategy, illustrator)

    def test_width_too_small(self):
        test_name = "width_one"
        quantity = self.simple_quantity
        strategy = Increasing()
        illustrator = GraphIllustrator(quantity, (58, 100), 50, COLORS)
        try: 
            self.helper(test_name, quantity, strategy, illustrator)
            assert False
        except InputError:
            assert True




"""
generate_graph
-file_path is empty string, space, chars that you cannot name a file
"""
