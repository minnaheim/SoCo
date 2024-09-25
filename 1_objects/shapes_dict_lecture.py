import math


def shape_density(thing,weight):
    return weight / call(thing,"area")

Shape = {
    "density": shape_density,
    "_classname":"Shape",
    "_parent":None
}



def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2



Square = {
    "perimeter":square_perimeter,
    "area": square_area,
    "_classname":"Square",
    "_parent":Shape
}


def square_new(name, side):
    new_object = {
        "name":name,
        "side":side,
        "_class":Square
    }
    return new_object



def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return (thing["radius"] ** 2) * math.pi


def circle_new(name,radius):
    new_object = {
        "name":name,
        "radius":radius,
        "_class":Circle
    }
    return new_object

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "_classname": "Circle",
    "_parent":Shape
}


def call(thing, key_name, *args):
    method = find(thing["_class"],key_name)
    return method(thing,*args)


def find(cls, key_name):
    if key_name in cls:
        return cls[key_name]
    if cls["_parent"]:
        return find(cls["_parent"],key_name)
    raise NotImplementedError("Missing method " + key_name)




a_square = square_new("quadrat",3)
n = a_square["name"]
p = call(a_square,"perimeter")
d = call(a_square,"density",100)
print(f"{n} has perimeter {p:.2f} and density {d:.2f}")


# a_circle = circle_new("kreis",5)
# examples = [a_square,a_circle]

# for each_example in examples:
#     n = each_example["name"]
#     p = call(each_example,"perimeter")
#     d = call(each_example,"density")
#     a = call(each_example,"area")
#     print(f"{n} has perimeter {p:.2f} and area {a:.2f}")