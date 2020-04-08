from typing import List
from src.illustrator import ColorProfile, Illustrator
from src.graph_generator import GraphGenerator
from src.graph_strategy import *
    
def select_image_size(size: str) -> int:
    """
    Selects the correct height and width of the graph in pixels.

    Args:
        size (string): one of the preset graph sizes.

    Returns:
        img_size (int): a positive integer representing width and height.
    """
    switcher = {
        "s": 250,
        "m": 500,
        "l": 750,
    }

def select_color_profile(cp: str)-> ColorProfile:
    """
    Selects the correct color profile.

    Args:
        cp (string): one of the preset color profiles.

    Returns:
        img_size (int): a positive integer representing width and height.

    TODO: add options!
    """
    background_color = (255, 255, 225, 255)
    border_color = (0, 0, 0, 255)
    bar_color = (33, 150, 243, 255)
    pointer_color = (243, 33, 45, 0)
    sorted_color = (33, 45, 243)
    return ColorProfile(background_color, border_color, bar_color, sorted_color, pointer_color)

def select_graph_strategy(case: str) -> GraphStrategy:
    """
    Instantiates the correct GraphStrategy.

    Args:
        case (string): one of the preset strategies.

    Returns:
        strategy(GraphStrategy): A instance of the correct GraphStrategy.
    """
    switcher = {
        "i": Increasing(),
        "d": Decreasing(),
        "n": NearlySorted(),
        "f": FewUnique(),
        "r": Random(),
        }

def handle_input(num_values: int, case: str, size: str, cp: str, file_path: str) -> None:
    """
    Transforms command line inputs into the specififed graph.

    Args:
        num_values (int): the number of values to be generated.
        case (string): one of the preset value patterns.
        size (string): one of the preset graph sizes.
        cp (string): one of the preset color profiles.
        file_path (string): the path relative to ./out to save the graph.

    Raises:
        InputError: num_values < 1.

    Returns:
        None.
    """
    image_size = select_image_size(size)
    border_size = 10
    colors = select_color_profile(cp)
    illustrator = Illustrator((image_size, image_size), border_size, colors)
    graph_strategy = select_graph_strategy(case)
    graph_generator = GraphGenerator(graph_strategy)
    graph_generator.generate_graph(num_values, illustrator, file_path)
    # generate frames
    # generate gif
