# when we define 2 functions where we include one in the other we either need to call both or def one by the other, but then loose the function
# this is repetitive, so we use closure
def original(value):
    print(f"The original value is {value}")




def logging(func):
    def _inner(value):
        print("-- before operation")
        func(value)
        print("-- before operation")

    return _inner

@logging
# original(10)
# original = logging(original)
