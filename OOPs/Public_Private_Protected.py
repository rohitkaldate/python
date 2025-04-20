### Public members:: Anyone can access this member either within the class or outside the class. By default all the memebers inside the class are public in the python.

##Within Class::
# class Test:
#     def __init__(self):
#         self.x=10
    
#     def m1(self):
#         print("m1 method")
#     def m2(self):
#         print(self.x)
#         self.m1()
# t=Test()
# t.m2()


##Outside class:
# class Test:
#     def __init__(self):
#         self.x=20
    
#     def m1(self):
#         print("m1 method")
#     def m2(self):
#         print(self.x)
#         self.m1()
# t=Test()
# t.m2()
# print(t.x)
# t.m1()


##Private Members::It is accessible only within the class and not from the outside of the class. It is declares using the "__x=10" as variable and "__m1(self)" as the method and is only accessible within the class where it is defined

# class Test:
#     def __init__(self):
#         self.__x=30 ##--> Private member variable 
#     def __m1(self): ##--> Private method 
#         print("Private method")
#     def m2(self):
#         print(self.__x)
#         self.__m1()
# t=Test()
# t.m2()

##Protected Members: It can be accessible within the class and from outside only the child class of the parent class can access. It can be declared as the "_x=10" as variable and "_m1(self)" for the method.
# class Test:
#     def __init__(self):
#         self._x=40  ##Protected Variablke
#     def _m1(self):  ##Protectred Method
#         print("Protected method")
#         # print(self._x)
# class Sub(Test):
#     def m2(self):
#         print(self._x)
#         self._m1()
# s=Sub()
# # s._m1()
# s.m2()

##Data Hiding:: hide your internal or essential data from someone.
# class Bank:
#     def __init__(self,total_balance):
#         self.__balance=total_balance    ##Private member
    
#     def m1(self):
#         print("Data hiding problem")
#         print(self.__balance)
        
# b=Bank(100000)
# b.m1()
