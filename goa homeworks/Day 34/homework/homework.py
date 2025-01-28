#1)
def fake_bin(x):
    res = ""
    
    for i in x:
        if int(i)<5:
            res += "0"
        else:
            res +="1"
    
    return res
#2)
def string_to_array(s):
    return s.split(" ")
#3)
def check(a, x):
    return x in a
#4)
def reverse_seq(n):
    return list(range(n,0,-1))
#5)
def count_by(x, n):
    res = []
    
    for i in range(1,n+1):
        res.append(x*i)
        
    return res