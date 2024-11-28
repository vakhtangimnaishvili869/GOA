
num = int(input("enter your number: "))
sum = 0

for i in range(num):
    sum = sum + i
print(sum)


correct_password = "123"
user_guess = input("Enter password: ")
counter = 0
while user_guess != correct_password:
    user_guess = input("Enter password: ")
    counter += 1
print("Access granted")
print("Your guess count:", str(counter))


counter = 0
my_num = 5
x = int(input("enter number: "))
while x != my_num:
    x = int(input("enter number: "))
    counter = counter + 1
print("guessed correct")
print(counter)
