#1)
#Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
def lovefunc( flower1, flower2 ):
    
    if flower1 % 2==0 and flower2 %2 != 0:
        return True
    elif flower2 % 2 ==0 and flower1 %2!=0:
        return True
    else:
        return False
#2)
#Write a function that takes an array of numbers and returns the sum of the numbers. 
def sum_array(a):
    return sum(a)
#3)
#Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
def paperwork(n, m):
    if n >= 0 and m>=0:
        return n * m
    elif n<0 or m<0 :
        return  0
#4)
# Clock shows h hours, m minutes and s seconds after midnight.  Your task is to write a function which returns the time since midnight in milliseconds.
def past(h, m, s):
    return s * 1000 + m * 1000  * 60 + h * 1000 * 60 * 60 
#5)
#Write a function which converts the input string to uppercase.


def make_upper_case(s):
    return s.upper()