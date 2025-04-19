# class Student:
#     school="SJS"
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def m1(self):
#         print(self.name)
#         print(self.roll)
#     @classmethod
#     def getm2(cls):
#         print(cls.school)
# s=Student("raj",1)
# s.m1()
# s.getm2()



##Has-A relationship
# class Engine:
#     def m2(self):
#         print("Engine functionality")
        
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m1(self):
#         print("Car has features of engine class")
#         self.engine.m2()
# c=Car()
# c.m1()

##IS-A Relationship:: Inheritence 
# class P:
#     def m1(self):
#         print("Parent")
# class C(P):
#     def m2(self):
#         print("Child")
        
# c=C()
# c.m1()
# c.m2()

# class P:
#     a=10
#     def __init__(self):
#         print("Parent constructor")
#         self.b=20
#     def m1(self):
#         print("Parent instance method")
#     @classmethod
#     def m2(cls):
#         print("Parent classmethod")
#     @staticmethod
#     def m3():
#         print("Parent staticmethod")
# class Child(P):
#     pass

# c=Child()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eatnddrink(self):
#         print("Person eat and drink")

# class Employee(Person):
#     def __init__(self,name,age,id,sal):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.sal=sal
        
#     def work(self):
#         print("Soft engineer")
        
#     def getEmp(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)
#         print(self.sal)
# e=Employee('Durga',48,123,1234556)
# e.eatnddrink()
# e.work()
# e.getEmp()

## Single Inheritance::
# class Parent:
#     def m1(self):
#         print("parent")
    
# class Child(Parent):
#     def m2(self):
#         print("Child")
# c=Child()
# c.m1()
# c.m2()


##Multilevel Inheritance::It is chain of classes. Inheriting multiple members of the multiple classes to the single child class
# class GrandParent:
#     def m0(self):
#         print("GrandParent")
# class Parent(GrandParent):
#     def m1(self):
#         print("parent")
    
# class Child(Parent):
#     def m2(self):
#         print("Child")
# c=Child()
# c.m0()
# c.m1()
# c.m2()


##Hierarchical Inheritance:: Inheriting members of single parent class into multiple child classes
# class GrandParent:
#     def m0(self):
#         print("GrandParent")
# class Parent(GrandParent):
#     def m1(self):
#         print("parent")
    
# class Child(GrandParent):
#     def m2(self):
#         print("Child")
# c=Child()
# p=Parent()
# c.m2()
# c.m0()
# p.m1()


##Multiple Inheritance:: Inheriting the multiple parent classes into the single child class

class P1:
    def m1(self):
        print("Parent1")

class P2:
    def m2(self):
        print("Parent2")
class Child(P1,P2):
    def m3(self):
        print("Child Accesing multiple parent classes")
        
c=Child()
c.m1()
c.m2()
c.m3()