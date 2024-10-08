# Using Debugger for this py file

a = 10  # a is saved as a frame
# if we put a break point here, without calling sum(3,4), then the sum isn't in locals

# IMPORTANT: variables and code are both data -> this function is stored as a frame


def sum(x, y):
    return x + y


my_sum = sum
print("stop")
print("after stop")

c = my_sum(3, 4)
print(c)

'''important to know: is both variables and functions are objects. '''
