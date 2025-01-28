#1)

#2)
def filter_list(l):
    return [i for i in l if type(i)==int]
#3)
def descending_order(num):
    num = str(num)
    return int("".join(sorted(num, reverse=True)))
#4)
def is_square(n):    
    if n < 0:
        return False
    return n ** 0.5 % 1 == 0
#5)
