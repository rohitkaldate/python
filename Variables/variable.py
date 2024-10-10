'''
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
#single variable name
a=5
print(a)
print(type(a))

#Multi words variable name
#1.camel case
myVariableName="Rohit"
print(myVariableName)

#2.Pascal case
MyName="Kaldate"
print(MyName)

#3.Snake case
my_name="Cisco"
print(my_name)

#Many values to multiple variables:
x,y,z="banana","mango" ,3
print(x)
print(y)
print(z)

#global Variable : it is declared outside the function
#It can be accessed by both function and outside function
h="Beautiful"
def myfunc():
    print("She is "+h)
    
myfunc()


# to create global variable inside function global keyword is used

def myfunc():
    global s
    s="Awesome"
myfunc()
print("She is "+s)

    