# import unittest
# import functions


def sign(value):
    if value < 0:
        return -1
    return 1


def t_minus_sign():
    assert sign(-3) == -1


def t_plus_sign():
    assert sign(19) == 1


def t_plus_sign_2():
    assert sign(1) == -1


results = {"pass": 0, "fail": 0, "error": 0}

print(globals())


def run_test(tests):
    for test in tests:
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(results)


def find_tests(prefix):  # example prefix = "t_"
    lists = []
    for (name, func) in globals().items():
        if name.startswith(prefix):
            print(name, func)
            lists.append(func)
        print(lists)
        return lists


find_tests("t_")

'''this is a special variable that checks if we are located in the specific file, so it wont be exectued when run from another file as an imported fileprin
when running py3 and printing globals, __name__ = "__main__"'''
if __name__ == "__main__":
    testing = find_tests('t_')
    run_test(testing)


# why is the function not being printed from the globals
