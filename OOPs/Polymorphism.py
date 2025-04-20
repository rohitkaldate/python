###Polymorphism:: It means nothing but the many/multiple forms. In this we are using the Overloading,Overriding

##Overloading:
### 1. Operator Overloading :: It is nothing but we are using the same operator for the multiple purposes . If we want to use the operators between the two objects then we require the magic method for that particular operator.

### Magic Mehtods::
# + --> __add__()
# - --> __sub__()
# * --> __mul__()
# / --> __div__()
# // --> __floordiv__()
# ** --> __pow__()
# % --> __mod__()
# += --> __iadd__()
# -= --> __isub__()

# ##Comparison Operators::
# < --> __lt__()  #less than
# <= --> __le__() #less than equals
# > --> __gt__() ##Gerater than
# >= --> __ge__() ##grater than equals

## "+ Operator example":::
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):  ##Magic Mehthod
#         total=self.pages+other.pages
#         return total
# b1=Book(100)
# b2=Book(400)
# print(b1+b2)

## "Comparision Operator"::
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def __gt__(self,other): ##Magic method
#         return self.marks>other.marks
# s1=Student("Rohit",96)
# s2=Student("Duraga",98)
# print(s1>s2)


## "*" Multiplication Operator::
# class Employee:
#     def __init__(self,name,salary_per_day):
#         self.name=name
#         self.salary_per_day=salary_per_day
    
#     def __mul__(self,other):
#         return self.salary_per_day*other.working_days
        

# class Timesheet:
#     def __init__(self,name,working_days):
#         self.name=name
#         self.working_days=working_days
    
#     def __mul__(self,other):
#         return self.working_days*other.salary_per_day

# e=Employee("durga",1000)
# t=Timesheet("durga",25)
# # print(e*t)
# print(t*e)



##Overriding:: Child class have all the members of the parent class by default  through inheritance. If child class is not satisfied with the parent class implementation  then it will be allowed to change the implementation as per the requirements .


## !. Method overriding :: Overrides the method which child does not satisfied with parents method
# class Parent:
#     def property(self):
#         print("Gold+Land+Power")
#     def marry(self):
#         print("Arrange")

# class Child(Parent):
#     def marry(self):
#         print("Love")
        
# c=Child()
# c.property()
# c.marry()

## 2.Constructor Overriding :: It will overrides the constructor of the parent class if the child is not satisfied with that constructor.

# class P:
#     def __init__(self):
#         print("Parent constructor")

# class Child(P):
#     def __init__(self):
#         print("Child Constructor")
# c=Child()