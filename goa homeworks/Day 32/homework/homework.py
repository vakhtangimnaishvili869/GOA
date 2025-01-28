#1)
def find_average(numbers):
    if numbers == []:
        return 0
    else:
        return sum(numbers ) / len(numbers)
#2)
def smash(words):
    return " ".join(words)
#3)
def grow(arr):
    num = 1
    
    for i in arr:
        num *= i
    return num
#4)
def hero(bullets, dragons):
    if bullets / dragons == 2 or bullets / dragons > 2:
        return True
    else:
        return False
#5)
def better_than_average(class_points, your_points):
    if sum(class_points) / (len(class_points) +1) < your_points:
        return True
    else:
        return False