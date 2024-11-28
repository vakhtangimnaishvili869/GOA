
a = range(20,50)
b = range(100,150)


c = range(20,30,2)
d = range(11,31,3)
for i in range(10):
    print("vato imnaishvili")
for i in range(10,30):
    print(i/2)
for i in range(40,60):
    print(i**3)

for i in range(5):
    user_num = float(input("Enter number: "))
    print(user_num)
name = input("Enter name: ")
for i in name:
    print(i)
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
range1 = range(num1, num2, num3)
for i in range1:
    print(i**2)

sum = 0
for i in range(5,16):
    sum += i
print(sum)