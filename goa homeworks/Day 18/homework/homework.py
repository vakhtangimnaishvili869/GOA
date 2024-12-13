#3
# num1 = int(input("enter num : "))
# num2 = int(input("enter num : "))
# if num1>num2:
#     print(num1)
# else:
#     print(num2)
#4
# number = float(input("enter any number : ")) 
# if number %2 == 0:
#     print("even")
# else:
#     print("odd")
#5
# number1 = int(input("enter any number : ")) 
# if number1>0:
#     print("selected number is possitive")
# else:
#     print("selected number is negative")
#6
# number2 =  int(input("enter any number : ")) 
# if number2 %5 == 0:
#     print("number is  diviseble by 5")
# else:
#     print("number is not  diviseble by 5")
#7
# for i in range(5):
#     num = int(input("enter number to see if its even or odd"))
#     print()
    
# if num %2 == 0:
#     print(num, " is even")
# else:
#     print( num ," is odd")
#8

correct_password = " goa best"
count = 0
usser_password = input(" enter password : ")
while usser_password != correct_password:
    count+=1
    usser_password = input(" enter password : ")
print(" password is correct")
print("u needed" , count , "tries")




#9
numb1 = float(input("Enter number: "))
numb2 = float(input("Enter number: "))
operator = input("Choose one operator: +, -, *, /, **, %  ")

if operator == "+":
    print(numb1, "+", numb2, "=", numb1+numb2)
elif operator == "-":
    print(numb1, "-", numb2, "=", numb1-numb2)
elif operator == "*":
    print(numb1, "*", numb2, "=", numb1*numb2)
elif operator == "/":
    if numb2 == 0:
        print("nothing can be divisible by 0")
    else:
        print(numb1, "/", numb2, "=", numb1/numb2)
elif operator == "**":
    print(numb1, "**", numb2, "=", numb1**numb2)
elif operator == "%":
    print(numb1, "%", numb2, "=", numb1%numb2)
else:
    print("Wrong operator")
