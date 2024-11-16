class Student:
    def __init__(self):
        self.name='Rohit'
        self.roll=101
        self.marks=96
    def talk(self):
        print("Hello I'm: ",self.name)
        print("Roll no is:",self.roll)
        print("And marks are: ",self.marks)

s=Student()
print(s.name)
print(s.roll)
print(s.marks)

s.talk()
