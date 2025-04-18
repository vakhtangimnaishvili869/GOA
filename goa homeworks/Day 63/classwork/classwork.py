age = int(input("Enter your age: "))

if age < 13:
    print("You are a kid")
elif age >= 13 and age <= 17:
    print("You are not adult yet")
else:
    print("You are an adult")