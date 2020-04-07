from src.draw_graph import *
from src.exceptions import InputError
from tests.image_testing import assert_image_equal
from typing import List
from PIL import Image

RELATIVE_FILEPATH = "images/tests/draw_graph/"
OUTPUT_FILEPATH = "./out/" + RELATIVE_FILEPATH
REFERENCE_FILEPATH = "./tests/images/draw_graph/"


def compare_images(fp_actual: str, fp_expected: str):
    actual = Image.open(fp_actual)
    expected = Image.open(fp_expected)
    assert_image_equal(actual, expected)
    
def draw_graph_helper(file_name: str, values: List[int], image_size: (int, int)):
    file_path = RELATIVE_FILEPATH + file_name
    fp_actual = OUTPUT_FILEPATH + file_name + ".png"
    fp_expected = REFERENCE_FILEPATH + file_name + ".png"
    draw_graph(values, image_size, 10, file_path)
    compare_images(fp_actual, fp_expected)

def test_values_one():
    file_name = "values_one"
    values = [50]
    image_size = (100, 100)
    draw_graph_helper(file_name, values, image_size)

def test_values_none():
    file_name = "values_none"
    values = []
    image_size = (100, 100)
    try:
        draw_graph_helper(file_name, values, image_size)
        assert False
    except InputError:
        assert True
  
def test_values_too_many():
    file_name = "values_too_many"
    values = [1, 2, 3, 4, 5, 6]
    image_size = (30, 30)
    try:
        draw_graph_helper(file_name, values, image_size)
        assert False
    except InputError:
        assert True


def test_size_zero():
    file_name = "size_zero"
    values = [0, 1, 2, 3, 4, 5]
    image_size = (0, 0)
    try: 
        draw_graph_helper(file_name, values, image_size)
        assert False
    except InputError:
        assert True

def test_size_small():
    file_name = "size_small"
    values = [230, 230, 230, 230, 230, 230, 230, 230, 230, 230]
    image_size = (250, 250)
    draw_graph_helper(file_name, values, image_size)

def test_size_medium():
    file_name = "size_medium"
    values = [480, 480,  480, 480, 480, 480, 480, 480, 480, 480,]
    image_size = (500, 500)
    draw_graph_helper(file_name, values, image_size)

def test_size_large():
    file_name = "size_large"
    values = [730, 730, 730, 730, 730, 730, 730, 730, 730, 730]
    image_size = (750, 750)
    draw_graph_helper(file_name, values, image_size)
