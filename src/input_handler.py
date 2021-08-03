from .graph_illustrator import ColorProfile, GraphIllustrator
from .graph_strategy import *
from .gif_strategies.selection_strategies import SelectionSort
from .gif_strategies.insertion_strategies import InsertionSort
from .gif_strategies.exchanging_strategies import BubbleSort, CocktailSort, CombSort, OddEvenSort, GnomeSort
from .gif_strategies.merging_strategies import MergeSort
from .graph_generator import GraphGenerator
from .gif_generator import GifGenerator


def select_color_profile(color: str) -> ColorProfile:
    """
    Selects the correct color profile.

    Args:
        color (str): used to select a preset color profile (red, blue or green).

    Returns:
        colors (ColorProfile): An instance of the correct ColorProfile.
    """
    background_color = (255, 255, 225)
    border_color = (0, 0, 0)

    red_bar_color = (244, 67, 54)
    red_cursor_color = (162, 54, 244)
    red_sorted_color = (153, 42, 34)
    red_fade_color = (251, 185, 180)

    blue_bar_color = (33, 150, 243)
    blue_cursor_color = (243, 126, 33)
    blue_sorted_color = (21, 94, 152)
    blue_fade_color = (172, 216, 250)

    green_bar_color = (76, 175, 80)
    green_cursor_color = (175, 129, 76)
    green_sorted_color = (48, 109, 50)
    green_fade_color = (188, 225, 189)
    switcher = {
        "red":
            ColorProfile(background_color, border_color, red_bar_color,
                         red_fade_color, red_sorted_color, red_cursor_color),
        "blue":
            ColorProfile(background_color, border_color, blue_bar_color,
                         blue_fade_color, blue_sorted_color, blue_cursor_color),
        "green":
            ColorProfile(background_color, border_color, green_bar_color,
                         green_fade_color, green_sorted_color,
                         green_cursor_color),
    }
    return switcher.get(color, None)


def select_graph_strategy(code: str) -> GraphStrategy:
    """
    Instantiates the correct GraphStrategy.

    Args:
        code (str): one of the preset strategy codes.

    Returns:
        strategy (GraphStrategy): An instance of the correct GraphStrategy.
    """
    switcher = {
        "increasing": Increasing(),
        "decreasing": Decreasing(),
        "nearly": NearlySorted(),
        "few": FewUnique(),
        "random": Random(),
    }
    return switcher.get(code, None)


def select_gif_strategy(code: str) -> GraphStrategy:
    """
    Instantiates the correct GifStrategy.

    Args:
        code (str): one of the preset strategy codes.

    Returns:
        strategy (GifStrategy): An instance of the correct GifStrategy.
    """
    switcher = {
        "selection": SelectionSort(),
        "insertion": InsertionSort(),
        "bubble": BubbleSort(),
        "cocktail": CocktailSort(),
        "comb": CombSort(),
        "gnome": GnomeSort(),
        "oddeven": OddEvenSort(),
        "merge": MergeSort(),
    }
    return switcher.get(code, None)


def handle_input(args) -> None:
    """
    Transforms command line inputs into the specififed graph.

    Args:
        args (Namespace): object holding parsed command line attributes.

    Modifies:
        ./sorting_visualized: saves a .png and a .gif to the filepath in args.

    Raises:
        InputError

    Returns:
        None.
    """
    colors = select_color_profile(args.color)
    illustrator = GraphIllustrator(args.quantity,
                                   (args.dimension, args.dimension),
                                   args.border, colors)
    graph_strategy = select_graph_strategy(args.input)
    graph_generator = GraphGenerator(graph_strategy)
    values = graph_generator.generate_graph(args.quantity, illustrator,
                                            args.path)
    gif_strategy = select_gif_strategy(args.algorithm)
    gif_generator = GifGenerator(gif_strategy, illustrator)
    gif_generator.generate_gif(values, args.path, args.speed)
