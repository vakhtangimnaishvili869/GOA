# 1
name = "hello"

try:
    print(username)
except NameError:
    print("username is not defined")

# 2
list1 = [1,2,3,4]

try:
    print(list1[4])
except IndexError:
    print("list index out of range")

# 3

try:
    print(int("12.23"))
except ValueError:
    print("ValueError: int not containes dot (.)")