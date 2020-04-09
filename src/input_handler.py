from typing import List
from src.graph_illustrator import ColorProfile, GraphIllustrator
from src.graph_strategy import *
from src.gif_strategies.selection_strategies import *
from src.graph_generator import GraphGenerator
from src.gif_generator import GifGenerator
    
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
    cursor_color = (243, 33, 45, 0)
    sorted_color = (33, 45, 243)
    return ColorProfile(background_color, border_color, bar_color, sorted_color, cursor_color)

def select_graph_strategy(choice: str) -> GraphStrategy:
    """
    Instantiates the correct GraphStrategy.

    Args:
        g_strategy (string): one of the preset strategies.

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

def select_gif_strategy(choice: str) -> GraphStrategy:
    """
    Instantiates the correct GifStrategy.

    Args:
        f_strategy (string): one of the preset strategies.

    Returns:
        strategy(GifStrategy): A instance of the correct GifStrategy.
    """
    switcher = {
        "s1": SelectionSort(),
        "s2": Heapsort(),
        "s3": Smoothsort(),
        "s4": Strandsort(),
        "s5": TournamentSort(),
        }

def handle_input(num_values: int, graph_choice: str, gif_choice: str, size: str, cp: str, file_path: str) -> None:
    """
    Transforms command line inputs into the specififed graph.

    Args:
        num_values (int): the number of values to be generated.
        graph_choice (string): one of the preset graph strategy inputs
        gif_choice (string): one of the preset gif strategy inputs
        size (string): one of the preset graph sizes.
        cp (string): one of the preset color profiles.
        file_path (string): the path relative to ./out to save the graph.

    Raises:
        InputError: 
            * num_values < 1.
            * number of values is too large for the image size

    Returns:
        None.
    """
    image_size = select_image_size(size)
    border_size = 10
    colors = select_color_profile(cp)
    illustrator = GraphIllustrator((num_values, image_size, image_size), border_size, colors)
    graph_strategy = select_graph_strategy(graph_choice)
    graph_generator = GraphGenerator(graph_strategy)
    graph_generator.generate_graph(num_values, illustrator, file_path)
    gif_strategy = select_gif_strategy(gif_choice)
    gif_generator = GifGenerator(gif_strategy, illustrator)
    # generate gif
