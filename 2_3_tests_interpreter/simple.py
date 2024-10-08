def same(num):
    return num

# this is an anonymous function - as data
# ["func", ["num"], ["bekommen, "num"],]

# this function is not anonymous, assign name
# ["setzen","same", ["func", ["num"], ["bekommen", "num"]]]


# if i want to call a function: ["call" "same", 3] -> function?, name, params
same(3+2)  # two ways to evaluate, eager (right away) and lazy (when needed) -> programming langs do eager

# if i want to call the function, need to use our predefined call function
# ["call", "same", ["addieren", 3, 2]]

# examples
# ["setzen", "add_two", "num1", "num2"] -> function
# ["addieren", "num1", "num2"]] -> body
# ["call", "add_two", 3,2] -> to call function
