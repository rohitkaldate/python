
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

#Create Function:
# def my_func():  #function creation
#     print("This is function")

# my_func()   #Calling function

#Passing arguments in function:
# def name(fname):    #Creating function with the single argument
#     print(fname+"kaldate")

# name("Rohit") #Calling function with single argument
# name("Amit") #Calling function with single argument
# name("Ajit") #Calling function with single argument

##Calling function using 2 arguments:
# def data(fname,lname):
#     print(fname + " " +lname)
# data("Rohit","Kaldate")
# data("Amit","Kaldate")
# data("Ajit","Kaldate")

#Arbitary arguments:
# def children(*kids):
#     print("Youngest brother is: "+kids[2])
# children("Rohit","amit","Ajit")


#Keyword arguments : Sending arguments with the key
# def kids(child2,child1,child3):
#     print("Youngest child is:"+ child3)
# kids(child1="Rohit",child3="amit",child2="Ajit")


##Default parameter value:
# def my_func(country="India"):
#     print("I am from ",""+country)

# my_func()
# my_func("USA")
# my_func("UK")


## Passing a list as an argument:

def my_function(food):
    for x in food:
        print(x)
    
fruits=["Apple","Mango","Kiwi","Cherry"]
my_function(fruits)