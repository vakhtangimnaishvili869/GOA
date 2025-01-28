#1)
#Your task is to create a function that does four basic mathematical operations.
def basic_op(operator, value1, value2):
    if operator == "+" :
        return value1 + value2
    elif operator == "-" :
        return value1 - value2
    
    elif operator == "*" :
        return value1 * value2
    elif operator == "/" :
        return value1 / value2
#2)
#Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling. You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
def litres(time):
    return int(time * 0.5)
#3)
#Given a year, return the century it is in.
def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
#4)
#Given an array of integers, return a new array with each value doubled.

def maps(a):
    res = []
    
    for i in a:
        res.append(i * 2)
        
    return res
#5)
def digitize(n):
    res = []
    
    for i in str(n):
        res.append(int(i))
        
    return res[::-1]

