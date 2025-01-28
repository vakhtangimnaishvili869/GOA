#1
#We need a function that counts the number of sheep present in the array 
def count_sheeps(sheep):
    sum = 0
    for i in sheep:
        if i == True:
            sum+=1
    return sum
        

#2
#Write a function that removes the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(" " , "")
#3
#You need to double the integer and return it.
def double_integer(i):
    return i * 2


#4)
#Make a function that will return a greeting statement that uses an input; your program should return,
def greet(name):
    return"Hello, "+name+" how are you doing today?"
#5) 
#Implement a function which convert the given boolean value into its string representation.

def boolean_to_string(b):
    return str(b)