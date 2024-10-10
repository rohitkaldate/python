'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray

'''
#str
x="Hello"
print(type(x))

#int
x=20
print(type(x))

#Float
x=20.5
print(type(x))

#Complex
x=20j
print(type(x))

# list
l=["apple","banana","cherry"]
print(type(l))

#tuple
t=("apple",2,"cherry",True)
print(type(t))

#range
r=range(6)
print(type(r))

#Dict:
d={"name":"Rohit","age":24,"address":"barshi","Mobie":7447218677}
print(d)
print(type(d))

#set
s={"apple","cherry","Kiwi"}
print(s)
print(type(s))


#frozenset
f=frozenset({"Apple","Mango","Orange"})
print(f)
print(type(f))

#bool

b=True
print(b)
print(type(b))


#Bytes

a=b"Hii"
print(a)
print(type(a))

#bytearray

arr=bytearray(6)
print(arr)
print(type(arr))
