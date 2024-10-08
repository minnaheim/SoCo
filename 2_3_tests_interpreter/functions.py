def add_(p1, p2):
    r = p1 + p2
    return r


def absolute_value(p1):
    if p1 > 0:
        return p1
    return -p1


# Testing Code
# V1:
x = add_(2, 3)
print(x)

# V2:
expected = 5
actual = add_(2, 3)
if actual != expected:
    print("you have a problem")

# V3:
expected = 5
actual = add_(2, 3)
assert actual == expected, "we have a problem"
