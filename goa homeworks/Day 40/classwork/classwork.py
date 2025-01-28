#1)
def get_count(sentence):
    count = 0
    
    for i in sentence:
        if i in "aeiou":
            count += 1
    return count
#2)
def disemvowel(string_):
    fixed = ""
    for i in string_:
        if i in "aeiou":
            string_.replace(i,"")
        elif i in "AEIOU":
            string_.replace(i,"")
        else:
            fixed +=i
    return fixed
#3)
def square_digits(num):
    num1 = ""
    
    for i in str(num):
        num1 += str(int(i)**2)
    
    return int(num1)
