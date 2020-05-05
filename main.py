import sys
import argparse
import dataclasses
from src.input_handler import handle_input

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Visualize Sorting",
        usage="%(prog)s [OPTION] [FILE]...",
        description="Generate bar chart visualizations of sorting algorithms"
        )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
        )
    parser.add_argument(
        "algorithm", metavar= "ALGORITHM",
        choices=["selection", "insertion", "bubble", "cocktail", "comb", 
        "gnome", "oddeven", "merge"],
        help = "sorting algorithm for the animation, one of {selection, insertion, bubble, cocktail, comb, gnome, oddeven, merge}"
        )
    parser.add_argument(
        "-q", "--quantity", metavar = "QUANTITY", default = "10", type=int,
        choices = range(1, 101),
        help = "number of values to be generated, must be within [0, 100]"
    )
    parser.add_argument(
        "-i", "--input", metavar = "INPUT", default="decreasing", 
        choices =["increasing", "decreasing", "nearly", "few", "random"],
        help = "pattern for generating the input list, one of {increasing, decreasing, nearly, few, random}"
    )
    parser.add_argument(
        "-d", "--dimension", default=500, type=int,
        help = "dimension (in pixels) for the animation (width & height)"
    )
    parser.add_argument(
        "-b", "--border", default = 25, type=int,
        help = "width (in pixels), for the border of the animation"
    )
    parser.add_argument(
        "-c", "--color", metavar = "COLOR", default="blue",
        choices = ["red", "blue", "green"],
        help = "colors for the animation, one of {red, blue, green}"
    )
    parser.add_argument(
        "-s", "--speed", metavar = "SPEED", default=1, type=int,
        choices = range(1, 101),
        help = "number of frames for each step of the animation, must be within [0, 100]"
    )
    parser.add_argument(
        "-p", "--path", default="./out/images/gif",
        help = "the file path and name relative to sorting_visualized/"
    )
    return parser

def main() -> None:
    """
    Parses user inputs to appropriate processing functions
    """
    parser = init_argparse()
    args = parser.parse_args()
    handle_input(args)
    
if __name__ == "__main__":
    main()
