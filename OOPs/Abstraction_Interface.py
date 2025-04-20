##Abstarct Method:: Method which has only decleration but not the implementation  is called as the abstract method. @abstarctmethod is the decorator required to declare the method as the abstract method and this decorator present in the module abc.
# from abc import abstractmethod
# class Vehicle:
#     @abstractmethod
#     def getWheels(self):
#         pass


##abstarct class:: Partially implemented classes are called as the abstract class.Every class/abstract class should be the child class of the ABC class. ABC is the class from the abc module

# from abc import ABC,abstractmethod 
# class Vehicle(ABC):
#     @abstractmethod
#     def getWheels(self):
#         pass


##Class without abstarct class but with the abstract method then it will help to create the object and instantiation is possible
# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass
# t=Test()
# t.m1()


##Interface:: Abstract class with the only abtractmethods and not the other methods iss called as interface.

# from abc import *
# class College(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
    
#     @abstractmethod
#     def m3(self):
#         pass

# class Durga(College):
#     def m1(self):
#         print("M1 implement")
#     def m2(self):
#         print("M2 Implement")
#     def m3(self):
#         print("M3 Implement")

# d=Durga()
# d.m1()
# d.m2()
# d.m3()