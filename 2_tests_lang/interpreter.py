import sys
import json


def do_addieren(args):
    assert len(args) == 2
    # dynamic dispatch, depending on the input, im calling the right operator
    left = do(args[0])
    right = do(args[1])
    return left + right


def do_betrag(args):
    assert len(args) == 1
    return abs(args[0])


def do(expr):
    if isinstance(expr, int):
        return expr
    assert isinstance(expr, list)
    if expr[0] == "addieren":
        return do_addieren(expr[1:])
    if expr[0] == "betrag":
        return do_betrag(expr[1:])
    assert False, "Unkown operation"

# to run this script, you need the python interpreter.py and code.tll


def main():
    program = ""
    assert len(sys.argv) == 2
    with open(sys.argv[1], "r") as source:
        program = json.load(source)
    print(program)
    result = do(program)
    print(result)


if __name__ == "__main__":
    main()
