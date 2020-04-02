import sys
import dataclasses

USAGE = f"Usage: {sys:argv[0]} [--help] | algorithm case size"

@dataclasses.dataclass
class Arguments:
    algorithm: str
    case: str
    size: str

def check_type(args):
    for field in dataclasses.fields(args):
        value = getattr(args, field.name)
        if type(value)  != field.type:
            print (f"Error: expected type {field.type} for {field.name}, "
            f"got {type(value)}")

def validate(args: List[str]):
    try:
        arguments = Arguments(*args)
    except TypeError:
        raise SystemExit(USAGE)

def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)

    if args[0] == "--help":
        print(USAGE)
    else:
        validate(args)


if __name__ == "__main__":
    main()
