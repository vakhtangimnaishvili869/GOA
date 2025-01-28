#1)
def area_or_perimeter(l , w):
    if l == w:
        return l**2
    else:
        return (l+w)*2
#2)
def other_angle(a, b):
    return 180 - (a+b)
#3)
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False
#4)
#5)
def sum_array(arr):
    if arr is None or len(arr) <= 1:
         return 0
    else:
         return sum(sorted(arr)[1:-2])