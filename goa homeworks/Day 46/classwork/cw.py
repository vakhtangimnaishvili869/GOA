# list - list's are ordered, changeable and dublicates are ok
# tuple - tuple's are ordered, unchangeable, dublicates are ok and it is faster than list
# set - set's are unordered, immutable but add and remove are ok and dublicates are not allowed

# 2
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# 2
def double_char(s):
    return "".join([i * 2 for i in s])

# 3
def get_age(age):
    return int(age[0])