##Table 
# i=1
# while i<=10:
#     print(i*2)
#     i=i+1


# using bresk statement in while loop:
# i=1
# while i<20:
#     print(i)
#     if i==12:
#         break
#     i=i+1

#Continue statement using while loop:

# i=1
# while i<10:
#     i=i+1
#     if i==5:
#         continue
#     print(i)

#Else in while 
# i=1
# while i<10:
#     print(i)
#     i=i+1

# else:
#     print("i is no longer less than 10")


# Prime no in range:
# n=int(input("Enter no: "))
# count=0
# n1=2
# while True:
#     x=True
#     for i in range(2,n1//2+1):
#         if n1%i==0:
#             x=False
#             break
#     if x==True:
#         print(n1)
#         count=count+1
#     if count==n:
#         break
#     n1=n1+1


# # Prime no or not:
# n=int(input("Enter no: "))
# x=True
# while True:
#     for i in range(2,n):
#         if n%i==0:
#             x=False
#             break
#     if x==True:
#             print("Prime no")
#             i=i+1
#     else:
#             print("Not a prime no")

#List of n Prime no:
n=int(input("Enter no: "))
count=0
n1=2
while True:
    x=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            x=False
            break
    if x==True:
        print(n1)
        count=count+1
    if count==n:
        break
    n1=n1+1