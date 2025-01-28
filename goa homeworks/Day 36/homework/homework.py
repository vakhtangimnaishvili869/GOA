#1)
def rental_car_cost(d):
    if d < 3:
        return d*40
    elif d >= 3 and d < 7:
        return (d*40)-20
    else:
        return (d*40)-50
#2)
def quarter_of(month):
    if month >= 1 and month <= 3:
        return 1
    elif month > 3 and month <= 6:
        return 2
    elif month >6 and month <= 9:
        return 3
    else:
        return 4
#3)
def remove_exclamation_marks(s):
    return s.replace("!", "")
#4)
def points(games):
    res = 0
    
    for i in games:
        if int(i[0]) > int(i[-1]):
            res +=3
        elif int(i[0]) == int(i[-1]):
            res += 1
            
    return res
#5)
def get_volume_of_cuboid(length, width, height):
    return width * height * length