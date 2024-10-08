import math
# this example is meant to showcase why and how to build an object structure?


# class is where we have the functions and the behaviour stored -> ex.: square is a class
# an object is the variable and the data is stored -> a_square is an object
#### Square ####


def square_perimeter(thing):
    return 4 * thing["side"]


def square_area(thing):
    return thing["side"] ** 2


def shape_density(thing, weight):
    return weight/call(thing, "area")

# because functions are data, we save them in a dictionary, and to call a specific funtion we def call.
# adding shape
Shape = {
    'density': shape_density,
    "_classname": "Shape",
    "_parent": None
}

# to seperate data from the variables, we do this:
# this way, we have a square which can have different perimeter and area, but is still part of the class square and parent shape
Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    '_classname': "Square",
    '_parent': Shape
}

# this is the new __init__ because it creates a new object, based on the class


def new_square(name, side):
    new_object = {
        'name': name,
        'side': side,
        # defined by previously created function
        # 'perimeter': square_perimeter,
        # 'area': square_area,

        # now, we just call up the class and the rest is done
        '_class': Square
    }
    return new_object

#### CIRCLE ####


def circle_perimeter(thing):
    return 2 * math.pi * thing['radius']


def circle_area(thing):
    return (thing['radius'] ** 2) * math.pi


def circle_new(name, radius):
    new_object = {
        'name': name,
        'radius': radius,
        'perimeter': circle_perimeter,
        'area': circle_area
    }
    return new_object


# define class function???

Circle = {
    'perimeter': circle_perimeter,
    'area': circle_area,
    '_classname': "Circle",
    '_parent': Shape
}

# create new objects
another_square = new_square('quadrat2', 3)
a_circle = circle_new('Kreis1', 5)

# separate search and call, thus define find


# f we define a parameter in a function with a leading *, it captures any “extra” values passed to the function that don’t line up with named parameters. 
# Similarly, if we define a parameter with two leading stars **, it captures any extra named parameters:
def call(thing, key_name, *args):
    method = find(thing["_class"], key_name)
    return method(thing, *args)


def find(cls, key_name):
    if key_name in cls:
        return cls[key_name]
    # constructor: 
    if cls["_parent"]:
        return find(cls["_parent"], key_name)
    raise NotImplementedError("Missing method " + key_name)


# getting bug because perimeter and area not floatable, aka str
# TODO: create both circle and square class and create example list, to execute below, and to get values, not actual funciton
a_square = new_square('Quadrat', 4)
n = a_square['name']
p = call(a_square, 'perimeter')
a = call(a_square, 'area')
d = call(a_square, 'density', 100)
print(f"{n} has perimeter {p}, area {a} and density {d}.")
