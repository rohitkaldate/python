class Student: #Class Created
    def __init__(self,x,y,z): #Constructor Defined
        self.name=x
        self.roll=y
        self.marks=z

    def talk(self): #Function Defined 
        print("Hello I'm: ",self.name)
        print("Roll no is:",self.roll)
        print("And marks are: ",self.marks)

# s=Student() #Object created for class Student(), s-is the reference variable,
# print(s.name)
# print(s.roll)
# print(s.marks)

s1 =Student("Pranil",111,98) ## Calling constructor with arguments:
print("Student is: ",s1.name,s1.roll,s1.marks)

s2=Student("Jay",112,99)
print("Student2:",s2.name,s2.roll,s2.marks)

s1.talk()

# s.talk() #Calling the function using the reference variable