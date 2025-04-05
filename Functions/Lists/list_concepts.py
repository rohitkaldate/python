##list Concepts::
# 1. **List**: A list is a collection of items that can be of any data type,
# # l=[]
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# print(l)
# print(type(l))

##Dynamic input::
# l=eval(input("enter list elements: "))
# print(l)

## Using list function::
# l=list("durga")
# print(l)

## String to list using split():::
# l="Python is Easy to Learn"
# s=l.split()
# print(s)

## Acccess elements of list using the index and slice operator
##using index operator::
# l=[10,20,30,40,50]
# print(l[0:3])
# print(l[-1])

##Using slice operator::
# l=[10,20,30,40,50,60,70,80]
# print(l[2:7])#step value is 1
# print(l[2:7:2]) #step value is 2
# print(l[4::2]) #step value is 2 start from index 4
# print(l[:1000])#Give full list
# print(l[4:0:2]) # Empty list
# print(l[::-1]) #Reverse lists 

#Prints index of elements
# l=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(l):
#     print(i)
#     i=i+1

# Print elements of list
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(i)

## Print even elements from the list
# l=[0,1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if i%2==0:
#         print("Even no is: ",i)
#     else:
#         print("odd no: ",i)

## Functions of the lists:
##len:returns no of elemnets in list
# l=[1,2,3,4,5]
# print(len(l))

#count(): returns the occurances of specified element in the list
# l=[1,2,3,4,5,6,1,3,4,1,4,1,1,2,3]
# print(l.count(1))
# print(l.count(2))
# print(l.count(3))
# print(l.count(4))
        
#index(): returns the indx of the 1st occurance of element
# l=[1,0,1,2,5,6,7,8,9]
# print(l.index(1))
# print(l.index(2))

##append():Adds the element in the list but at the end only
# l=[1,2,30,50,60]
# l.append(40)
# l.append(70)
# l.append(80)
# print(l)

##WAP to add the numbers to the list which are divisible by 10
# l=[]
# for i in range(1,101):
#     if i%10==0:
#         l.append(i)
# print(l)

#insert(): it adds the elemnt in list at specified index
# l=[10,20,30,40,50]
# l.insert(1,77)
# print(l)

##extend()::it will add the one list to another
# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)


##remove():: removes specified elements in the list then only 1st occurance of the element is removed
# l=[1,2,3,1,1,4,5]
# l.remove(1)
# print(l)


##pop():: It removes element present at last
# l=[10,20,30,40]
# print("Removed element: ",l.pop())
# print(l)

##pop(index):: It removes & returns the element with specified index
# l=[10,20,30,40]
# print(l.pop(2))
# print(l)

##clear():: removes all elements
# l=[1,2,3,4,5]
# print(l)
# l.clear()
# print(l)


##reverse()::it reverse the list
# l=[10,20,30,40]
# l.reverse()
# print(l)

##reversed():: built in function
# l=[10,20,30,40]
# a=reversed(l)
# l1=list(a)
# print(l1)

## sort():: it will sort the elements of the list in the ascending order for numbers and for the albhabetical order for the characters
# l=[102,3,1,54,9,0,30,20]
# l.sort()
# print(l)
# l=["Man","App","Xat","Cat","Bag"]
# l.sort()
# print(l)

## sorted()::built in function
# l=[1,204,40,50,0,2,30,20,10]
# l1=sorted(l)
# print(l1)


## WAP to removes the duplicate elemnts from the list

l=[10,20,30,40,20,10,30,40,50,10,10,20,30,40,50,50]
s=set(l)
print(s)
l1=list(s)
print(l1)
