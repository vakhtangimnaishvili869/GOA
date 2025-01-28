#1)
list1 = [ i for i in range(1, 101)]
print(list1)

#2)
list2 = [i for i in range(1,101) if i%2 != 0]
print(list2)
    
#3) 
list3 = ["levan","vato", "gio","davit","avto"]
list4 = ["#" + .replace("a",) for i in list2]
print(list3)
#4)
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
#5)
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "red":
        return "green"
    elif current == "yellow":
        return "red"
