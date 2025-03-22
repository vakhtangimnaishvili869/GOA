
def get_planet_name(id):
 
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name


def move(position, roll):
    return position + roll * 2


def enough(cap, on, wait):
    wait = wait - (cap - on)
    if wait < 0:
        return 0
    else:
        return wait
    

def between(a,b):
    return [i for i in range(a, b + 1)]


def say_hello(name):
    return "Hello, " + name

li = [1,2,3,4,5,50,100,200,300,400,50]
print(list(filter(lambda x: x >= 40, li)))
print(list(map(lambda x: x ** 2, li)))

ll = ["apple", "banana", "cherry", "kiwi", "mango"]
print(list(filter(lambda x: x.endswith("a"), ll)))
