#1)
def remove_char(s):
    return s[1 : -1]
#2)
def square_sum(numbers):
    
    listn = []
    for i in numbers:
        listn.append(i**2)
    return sum(listn)    

#3)
def find_smallest_int(arr):
    return min(arr)
#4)
def string_to_number(s):
    return int(s)

#5)
def summation(num):
    sum1=0
    for i in range(1 , num+1):
        sum1 += i
    return sum1
#6)
def greet():
    return "hello world!"