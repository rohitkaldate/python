# for i in range(3):
#     for j in range(3):
#         if i==j:
#             continue
#         print(i,j)

# s="Learning python is easy"
# l=s.split()
# print(l)
# l1=l[::-1]
# print(l1)
# print(' '.join(l1))

# l=s.split()
# print(l)
# l1=[]
# for i in l:
#     l1.append(i[::-1])
# print(l1)
# op=' '.join(l1)
# print(op)

# s="Durgasoft"
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+2

# i=1
# while i<len(s):
#     print(s[i])
#     i=i+2

# print("Even: ",s[::2])
# print("Odd: ",s[1::2])

# s="AABACBB"
# l=[]
# for i in s:
#     if i not in l:
#         l.append(i)
# print(l)
# for i in l:
#     print("{} occurs {} times".format(i,s.count(i)))


# s="DURGASOFTWARE"
# v={'a','e','i','o','u','A','E','I','O','U'}
# d ={}
# for i in s:
#     if i in v:
#         d[i]=d.get(i,0)+1
# print(d)


### Anagram means the string 2 have the same cahracters as string 1 but the order of character is not fixed
# s1="raja"
# s2="jar"
# if sorted(s1)==sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagrams")


## Pallindrome or not:

# s=input("Enter str: ")
# if s==s[::-1]:
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")

#Print all keywords in the python::
 # # import keyword 
# # r=keyword.kwlist
# # print(r)

# a=10.5
# print(a)
# print(type(a))
# s="rohit"
# print(s)
# print(type(s))
# print(s[0:])
# print(s[:1])
# print(s[:])
# print(s[1:5])
# print(int("10"))
# print(int(False))

#Print char's of the string
# s="rohit"
# for i in s:
#     print(i)

# for x in range(10):
#     print("rohit")

# for i in range(0,11):
#     # print(i)
#     # i+=1
#     if i%2==0:
#         print("Even:",i)
#     else:
#         print("Odd: ",i)

#print even no's in given range::
# for i in range(0,21):
#     if i%2==0:
#         print(i)
#         i+=1

#Print sum of given list 
# l=eval(input("Enter no's: "))
# sum=0
# for i in l:
#     sum =sum+i
# print(sum)

# i=0
# while i<=10:
#     print("Hello")
#     i=i+1

#Table of numbers: -->
# i=1
# while i<11:
#     print(i*2)
#     i=i+1

# x=1
# while x<=20:
#     if x%3==0:
#         print(x)
#     x=x+1

# Sum of n natural numbers:
# n=int(input("Enter a number: "))
# sum=0
# i=1
# while i<=n:
#     sum =sum+i
#     i=i+1
# print(sum)

#Sum using for loop -->
# n=int(input("Enter no: "))
# sum=0
# for i in range(n):
#     sum=sum+i
#     i=i+1
# print(sum)

#Infinite loop: -->
# i=1
# while True:
#     print("hello",i)
#     i=i+1
#     if i==3:
#         break

#print table of number take input from user -->
# n=int(input("Enter a number: "))
# i=1
# while i<11:
#     print(n*i)
#     i=i+1

# Nested Loop::
# for i in range(3):
#     for j in range(2):
#         print("Hello")


#WAP to print * in single line -->
# n=int(input("Enter a no: "))
# for i in range(n):
#     print('* ',end='')

# Print the * in sqaure pattern
# n=int(input("Enter a no: "))
# for i in range(n):
#     print('* '*n)

# Print * in right angle triangle
# n=int(input("Enter a no: "))
# for i in range(n):
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# Print the inverted right angle triangle
# n=int(input("Enter a no: "))
# for i in range(n):
#     print('* '*(n-i))
    
# Print pyramid of the *
# n=int(input("Enter a no: "))
# for i in range(n):
#     print(' '*(n-i-1)+'* '*(i+1))

#Inverted Pyramid: -->
# n=int(input("Enter a no: "))
# for i in range(n):
#     print(' '*i+'* '*(n-i))

#Code for the break statement: -->
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             break
#         print(i,j)

#Code for the continue statement -->
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             continue
#         print(i,j)

#For loop with if and break statements: -->

# list = [10,20,30,400,50]
# for i in list:
#     if i>60:
#         print("Insurance required ")
#         break
#     print(i)
# else:
#     print("Congratulations ")


#WAP to check given no is prime or not prime -->
# n=int(input("Enter a no: "))
# x=True
# for i in range(2,n):
#     if n%1==0:
#         x=False
#         break
# if x==True:
#     print("prime no: ",n)
# else:
#     print("Not Prime no: ",n)

#WAP to display characters of string -->
# s="Rohit"
# for i in s:
#     print(i)


# s="abcdabcd"
# print(s.find('a')) ## find from left to right
# print(s.rfind('a')) #finds from right to left backward dirn
# print(s.index('b')) #Works same as find
# print(s.rindex('a')) # works same as rfind()

#Count char in string using count() -->
# s="ABCDABABAABBCCDD"
# print(s.count('A'))
# print(s.count('B'))
# print(s.count('C'))
# print(s.count('D'))

#Replace string characters using the replace() -->
# s="ABCDABABAABBCCDD"
# print(s.replace('A','B'))
# a="durga softwatare solutions"
# print(a.replace(' ',''))

## Split() and Join():::
#split(): -->
# s="durga softwatare solutions"
# l=s.split()
# print(l)
# for i in l:
#     print(i)
    
#join(): -->
# s="durga softwatare solutions"
# l=s.split()
# print(l)
# d=' '.join(l)
# print(d)

## Changing the case of the string from one to another::
# s="Durga Softwatare Solutions"
# print(s.upper())#to uppercase
# print(s.lower())#to lowercase
# print(s.swapcase()) #Upper to lower & lower to upper
# print(s.title()) #Every 1st letter is capital
# print(s.capitalize()) #Only 1st char of string is capital


##WAP to check if the strinf are equal or not -->
# s1=input("Enter 1st: ")
# s2=input("Enter 2nd: ")
# if s1.lower() == s2.lower():
#     print("Equal")
# else:
#     print("Not Equal")

##WAP to check entere usr and password is valid or not -->
# usr=input("Enter uname:")
# passwd=input("Enter pass:")

# if usr.lower()=="durga" and passwd =='Raj':
#     print("Valid credentials")
# else:
#     print("Invalid Credentials")

##startswith and endswith:: -->
# s="Durga Software Solution"
# print(s.startswith('Durga'))
# print(s.endswith('Software'))


#String Methods:: -->
# strip()
# rstrip()
# lstrip()
# find()
# index()
# rfind()
# rindex()
# count()
# replace('a','b')
# split()
# join()
# upper()
# lower()
# swapcase()
# title()
# capitalize()
# startswith()
# endswith()