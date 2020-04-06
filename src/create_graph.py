from typing import List
from src.draw_graph import draw_graph
from src.generate_values import generate_values


def get_img_size(size: str) -> int:
    """
    Picks the  height and width of the graph in pixels. based on the size.

    Args:
        size (string): one of the preset graph sizes.

    Returns:
        img_size (int): a positive integer representing width and height
        
    TODO: 
        * consider allowing user input?- do switch statements have an else case in python?
    """
    switcher = {
        "s": 250,
        "m": 500,
        "l": 750,
    }


def handle_input(num_values: List[int], case: str, size: str, file_name: str) -> None:
    """
    Transforms command line inputs into the specififed graph

    Args:
        num_values (int): the number of values to be generated
        case (string): one of the preset value patterns
        size (string): one of the preset graph sizes
        file_path (string): the path relative to ./out to save the graph

    Raises:
        InputError: num_values < 1

    Returns:
        None

    TODO:
        * do we need to store information about starting column and column width for image manipulation?
        * will algorithm handling happen here or elsewhere...
    """
    border_width = 10
    img_size = get_img_size(size)
    maximum_value = img_size - 2*border_width
    values = generate_values(case, num_values, maximum_value)
    draw_graph(img_size, values, border_width, file_name)
