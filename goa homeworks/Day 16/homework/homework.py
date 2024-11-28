#Write a program that uses a while loop to count from 1 to 10 and prints each number.
i = 1
while i<=10:
    print(i)
    i+=1

#Prompt the user to enter a password. Keep asking until they enter the correct password.
# correct_password="12345"
# password = ""
# while password != correct_password:
#     password = input("enter password : ")
# print("password is correct")

#Create a program that keeps asking for a username and password until both are correct.

# correct_pass = "123"
# correct_user = "vato"

# passw = ""
# user = ""
# while passw != correct_pass or user != correct_user :
#     passw = input("enter password")
#     user = input("enter username")
# print("user and password is correct")   

#Use a while loop to calculate the factorial of a given number.
number = int(input("enter number to calculate its factorial : "))
factorial = 1
i = number

while i>0:
    factorial*= i 
    i-= 1
print(f"The factorial of {number} is {factorial}.")