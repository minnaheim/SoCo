import sys
import json


def do_sequenz(env,args):
    assert len(args) > 0
    result = None
    for expr in args:
        result = do(env,expr)
    return result



def do_setzen(env, args):
    assert len(args) == 2
    assert isinstance(args[0],str)
    var_name = args[0]
    value = do(env, args[1])
    env[var_name] = value
    return value


def do_bekommen(env, args):
    assert len(args) == 1
    assert isinstance(args[0],str)
    assert args[0] in env, f"Variable name {args[0]} not found"
    value = env[args[0]]
    return value


def do_addieren(env, args):
    assert len(args) == 2
    left = do(env, args[0])
    right = do(env, args[1])
    return left + right

def do_betrag(env, args):
    assert len(args) == 1
    val = do(env,args[0])
    return abs(val)


def do(env, expr):
    if isinstance(expr,int):
        return expr
    assert isinstance(expr,list)
    if expr[0] == "addieren":
        return do_addieren(env, expr[1:])
    if expr[0] == "betrag":
        return do_betrag(env, expr[1:])
    if expr[0] == "setzen":
        return do_setzen(env, expr[1:])
    if expr[0] == "bekommen":
        return do_bekommen(env, expr[1:])
    if expr[0] == "sequenz":
        return do_sequenz(env,expr[1:])
    assert False, "Unknown operation"


def main():
    program = ""
    assert len(sys.argv) == 2, "usage: python interpreter.py code.tll"
    with open(sys.argv[1], "r") as source:
        program = json.load(source)
    #print(program)
    result = do({}, program)
    print(result)


if __name__ == "__main__":
    main()