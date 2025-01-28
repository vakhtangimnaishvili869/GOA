#1)
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
#2)
def is_divisible(n,x,y):
    if n % y == 0 and  n  % x == 0  :
        return True
    else:
        return False
#3)
def count_sheep(n):
    str = ""
    
    if n == 0:
        return ""
    
    for i in range(1,n+1):
        str += f"{i} sheep..."
        
    return str
#4)
def get_grade(s1, s2, s3):
    average = (s1+s2+s3)//3
    if average >= 90:
        return "A"
    elif average < 90 and average >= 80:
        return "B"
    elif average < 80 and average >= 70:
        return "C"
    elif average < 70 and average >= 60:
        return "D"
    else:
        return "F"
#5)
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"