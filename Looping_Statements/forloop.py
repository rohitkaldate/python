fruits=["apple","banana","kiwi","cherry"]
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

adj=["red","big","tasty"]
fruit=["apple","mango","kiwi"]

for x in adj:
    for i in fruit:
        print(x,i)

