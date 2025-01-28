#1)
def abbrev_name(name):
    name = name.split(" ")
    return name[0][0].upper() + "." + name[1][0].upper()
#2)
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + "plays banjo"
    else:
        return name + "does not play banjo"
#3)
def simple_multiplication(number) :
    if number %2 == 0:
        return number*8
    else:
        return number*9
#4)
def find_needle(haystack):
    index = haystack.index("needle")
    return f"found the needle at position {index}" 
#5)
def invert(lst):
    noq = []
    
    for i in lst:
        noq.append(-i)
        
    return noq





