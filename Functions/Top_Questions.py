##WAP to print the factorial of the number using the return :::
# n=int(input("Enter no : "))
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# f=fact(n)
# print(f)


##WAP to print the factorial of the number using the recursive function:::
# n = int(input("Enter no : "))

# def fact(n):
#     if n == 0:
#         res=1
#     else:
#         res=n*fact(n-1)
#     return res
# print(fact(n))


###WAP to check the number is prime or not::::

n = int(input("Enter no : "))
x=True
for i in range(2,n):
    if n%i==0:
        x=False
        break
if x==True:
    print("Prime")
else:
    print("Not Prime")