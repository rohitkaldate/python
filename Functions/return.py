# Factorial no:

def fact(n):
    res=1
    while n>=1:
        res*=n
        n-=1
    return res
f=fact(3)
print(f)