#3
num1= int(input("enter any number : "))
num2= int(input("enter any number : "))
num3= int(input("enter any number : "))
if num1>num2 and num3:
    print(num1)
elif num2>num1 and num3:
    print(num2)
else:
    print(num3)

#4
Num = int(input("enter a score between 0-100 "))
if Num>89 and Num<=100:
    print("your score is A")
elif Num>79 and Num<=89:
    print("your score is B")
elif Num>69 and Num<=79:
    print("your score is C")
elif Num>59 and Num<=69:
    print("your score is D")
else:
    print("your score is F")
    if Num>100:
        print("your score is not correct ,check again")
        

#5

number1 = int(input("enter any number : ")) 
if number1>0:
    print("selected number is possitive")
elif number1==0:
    print(" selected number is zero")
else:
    print("selected number is negative")

#6


#7

NUMB = int(input("enter number to see if it is prime : "))
count = 0
for i in range(1, NUMB+1):
    if NUMB % i == 0:
        count+=1
if count==2:
    print(NUMB, "is  prime number" )
else:
    print(NUMB, "is  not prime number" )

#8
list1 = 1, 2 ,3 ,4 ,5 
print(list1[0])
print(list1[2])
print(list1[4])

# 9
list2= 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9, 10 ,11 ,12 ,13, 14, 15 ,16 ,17 ,18 ,19, 20
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
print(list2[5])
print(list2[6])
print(list2[7])
print(list2[8])
print(list2[9])
print(list2[10])
print(list2[11])
print(list2[12])
print(list2[13])
print(list2[14])
print(list2[15])
print(list2[16])
print(list2[17])
print(list2[18])
print(list2[19])