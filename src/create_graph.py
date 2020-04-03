from src.draw_graph import draw_graph
from src.generate_values import generate_values


def get_img_size(size):
    """
    Picks the  height and width of the graph in pixels. based on the size.

    Args:
        size (string): one of the preset graph sizes.

    Returns:
        img_size: a positive integer 
        
    TODO: 
        * consider allowing user input?- do switch statements have an else case in python?
    """
    switcher = {
        "s": 300,
        "m": 600,
        "l": 1200,
    }


def handle_input(num_values, case, size):
    """
    Transforms command line inputs into the specififed graph

    Args:
        num_values (int): the number of values to be generated
        case (string): one of the preset value patterns
        size (string): one of the preset graph sizes

    TODO:
        * determine if it returns graph or writes to file?
        * do we need to store information about starting column and column width for image manipulation?
        * will algorithm handling happen here or elsewhere...
    """
    border_width = 5
    img_size = get_img_size(size)
    maximum_value = img_size - 2*border_width
    values = generate_values(case, num_values, maximum_value)
    draw_graph(img_size, values, border_width)
