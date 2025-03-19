# fruits=["apple","banana","kiwi","cherry"]
# for x in fruits:
#     print(x)

# for i in 'apple':
#     print(i)


#Break statement in for loop:
# for i in fruits:
#     print(i)

#     if i=="banana":
#         break

#print after break:
# for x in fruits:
#     if x=="cherry":
#         break
#     print(x)


#conitunue statement using for loop:
# for c in fruits:
#     if c == "kiwi":
#         continue
#     print(c)

#Range function in for loop:
#This range( ) function starts taking the values from the 0.

# for i in range(10):
#     print(i)

#range with starting value and also used if condition to print even no's:
# for i in range(2,10):
#     if(i%2==0):
#         print("Even no's from 2 to 10 are: ",i)

#Nested for loop:

# adj=["red","big","tasty"]
# fruit=["apple","mango","kiwi"]

# for x in adj:
#     for i in fruit:
#         print(x,i)

# print pattern in :
# * * *
# * * *
# * * *

# n=int(input("Enter the number: "))
# for i in range(n):
#     print("* "*n)


# Print pattern like below:
# *
# * *
# * * *
# n=int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()

# n=int(input("Enter the number: "))
# for i in range(n):
#     print(' '*(n-i-1)+"* "*(i+1))  # print spaces and then stars

#List of n Prime no:
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

n=int(input("Enter no: "))

### Nested for loop with break statement::

# for i in range(n):
#     for j in range(3):
#         if i==j:
#             break
#         print(i,j)

## Nested for loop with continue statement:

for i in range(n):
    for j in range(3):
        if i==j:
            continue
        print(i,j)
