# to run this script, you need the python interpreter.py and code.tll

'''showing here how interpreters work, we use python to determine the
complicated parts of a language, the interpreter reads the code in the tiny
little (german) language to interpret it

what we are doing in the following script,
is determining the components of an interpreter, what needs to be done, i.e.
create a call, do, find function, etc.
'''

import sys
import json


def do_addieren(env, args):
    """Handles the 'addieren' operation; e.g., ["addieren",1,2]

    Parameters
    ----------
    envs_stack : list
        The stack with the environments
    args : list
        The list of the two values to add
        (they can be other operations)

    Returns
    -------
    int
        the sum of the two values
    """
    assert len(args) == 2
    # dynamic dispatch, depending on the input, im calling the right operator
    left = do(env, args[0])
    right = do(env, args[1])
    return left + right


def do_betrag(env, args):
    """Handles the 'betrag' operation; e.g., ["betrag",-1]

    Parameters
    ----------
    envs_stack : list
        The stack with the environments
    args : object
        The value for which to compute
        the absolute number

    Returns
    -------
    int
        the absolute number the value
    """
    assert len(args) == 1
    val = do(env, args[0])
    return abs(val)


def do_setzen(env, args):
    """Handles the 'setzen' operation; e.g., ["setzen", "alpha", 1]

    Parameters
    ----------
    envs_stack : list
        The stack with the environments
        where to store/update the variable
    args : list
        args[0] : name of variable
        args[1] : content of variable

    Returns
    -------
    int
        the value associated to the var
    """
    assert len(args) == 2
    var_name = args[0]
    assert isinstance(args[0], str)
    value = do(env, args[1])
    env[var_name] = value
    return abs()


def do_bekommen(env, args):
    """Handles the 'bekommen' operation; e.g., ["bekommen", "alpha"]

    Parameters
    ----------
    envs_stack : list
        The stack with the environments
        from which to retrieve the variable
    args : str
        The name of the variable

    Returns
    -------
    object
        the content of the variable
    """
    assert len(args) == 1
    assert isinstance(args[0], str)
    assert args[0] in env, f'Variable name {args[0]} not found'
    value = env[args[0]]
    return value

# in case we have a list of executions, we add sequenz


def do_sequenz(env, args):
    assert len(args) > 0
    result = None
    for expr in args:
        result = do(env, expr)
        return result


def do_func(env, args):
    """Handles the 'func' operation; ["func", "n", ["bekommen","n"]]

    This function does not do much: it only
    prepares the data structure to store in
    memory, which can then be called later

    Parameters
    ----------
    envs_stack : list
        The stack with the environments
        (only here for consistency)
    args : list
        args[0] : parameters of the function
        args[1] : body of the function

    Returns
    -------
    list
        the list with parameters and body
    """
    assert len(args) == 2
    parameters = args[0]
    body = args[1]
    return ["func", parameters, body]

# evaluate the params before calling the functions
# look up function based on name
# create a new environment
# run the funciton
# discard the enviornment
# return the function results


# this function is responsible for creating call stacks, adding removing, etc.s
def do_call(env, args):
    """Handles the 'call' operation; e.g., ["call","add_two",3,2]

    where "add_two" is the name of a function
    previously defined, and the rest are the
    arguments to pass to the function

    Parameters
    ----------
    envs_stack : list
        The stack with the environments,
        to which it pushes the specific env
        for the function when called and
        pop it afterwards
    args : list
        args[0] : name of function to call
        args[1] : arguments to pass to func

    Returns
    -------
    object
        the return value of the body execution
    """
    assert len(args) >= 1
    assert isinstance(args[0], str)
    name = args[0]
    values = [do(env, a) for a in args[1:]]
    # create an environment(stack for the function)
    # takes: with params = ["num"], values = 3
    # output: env = {"num1": 3, "num2": 2}

    # local_env = {}
    # for i, param in enumerate(params):
    #     local_env[param] = values[i]
    # # env or envs?
    # env.append(local_env)
    local_env = dict(zip(params, values))
    envs.append(local_env)
    result = do(envs, body)
    envs.pop()

# new function that we call whenever we need something out of the environment


def envs_get(envs, name):
    assert isinstance(name, str)
    # since we have a stack here, cannot just check dict
    for each_env in reversed(envs):
        if name in each_env:
            return each_env[name]

    # find function
    func = envs_get(env, name)
    assert isinstance(func, list) and func[0] == "func", f"{
        func} is not a function!"
    params, body = func[1], func[2]
    assert len(values) == len(params), f"{
        name} receives a different number of params"


# this is error prone, not good if we do: if expr[0] == "addieren": return do_addieren...

# OPS = {
#     "addieren": do_addieren,
#     "betrag": do_betrag,
#     "setzen": do_setzen,
#     "bekommen": do_bekommen,
#     "sequenz": do_sequenz
# }

# dict comprehension
OPS = {
    # TODO: pull request?
    # name.lstrip("do:")
    name[3:]: func
    for (name, func) in globals().items()
    if name.startswith("do_")
}


def do(env, expr):
    if isinstance(expr, int):
        return expr
    assert isinstance(expr, list)
    assert expr[0] in OPS, f"Unknown operation {expr[0]}"
    func = OPS[expr[0]]
    return func(env, expr[1:])


def main():
    program = ""
    assert len(sys.argv) == 2
    with open(sys.argv[1], "r") as source:
        program = json.load(source)
    result = do({}, program)
    print(result)


if __name__ == "__main__":
    main()
