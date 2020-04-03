import sys
import dataclasses

USAGE = f"Usage: {sys:argv[0]} [--help] | algorithm case size"

@dataclasses.dataclass
class Arguments:
    algorithm: str
    case: str
    size: str

# TODO: discover if this is needed or can be deleted?
def check_type(args):
    """
    Validates the type of all the args

    Args:
        args (List[str]): list of arguments from the user

    """
    for field in dataclasses.fields(args):
        value = getattr(args, field.name)
        if type(value)  != field.type:
            print (f"Error: expected type {field.type} for {field.name}, "
            f"got {type(value)}")

def validate(args: List[str]):
    """
    Attempts to build an Arguments object out of the args receieved from user.

    Args:
        args (List[str]): list of arguments from the user

    Raises:
        TypeError: one of the arguments is of incorrect type
    """
    try:
        arguments = Arguments(*args)
    except TypeError:
        raise SystemExit(USAGE)

def main() -> None:
    """
    Passes user inputs to appropriate processing functions
    """
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)

    if args[0] == "--help":
        print(USAGE)
    else:
        validate(args)


if __name__ == "__main__":
    main()
