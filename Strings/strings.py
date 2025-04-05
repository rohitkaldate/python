s="Rohit"
s1="Kaldate"
# print(s)
# print(type(s))
# print(len(s))

## Print characters of the given string::
# for i in s:
#     print("Characters are: ",i)


### Slice Operator::::

# print(s[0:])
# print(s[:])
# print(s[1:3])
# print(s[:4])

###Concatenation::::
# name=s+s1
# print(name)

### Repetation:::::
# print(s*3)

### find():
# print(s.find("i"))

###rfind()::::
# print(s.rfind("i"))

a='abcabcabcabc'
# print(a.count('a'))  # count of 'a' in the string
# print(a.find('d'))  # index of first 'a' in the string


# print(a.replace('a','r')) # replace 'a' with 'r' in the string
# print(a.replace('b','c')) # replace 'b' with 'c' in the string
# print(a.replace('c','b')) # replace 'c' with 'b' in the string



### split() and join()

ch="Durga Software solutions"
# print(ch.split())
# print(''.join(ch))

#### upper(),lower(),swapcase(),title(),capitalize()
# print(ch.upper())
# print(ch.lower())
# print(ch.swapcase())
# print(ch.title())
# print(ch.capitalize())

# x="Raj"
# y="Raj"
# if x==y:
#     print("Both strings are same")
# else:
#     print("Both strings are not same")


# n=input("Enter string: ")
# op=n[0].upper()+n[1:len(n)-1].lower()+n[-1].upper()
# print(op)

s1=input("Enter s1: ")
# s2=input("Enter s2: ")

# # if s1==s2:
# #     print("Equal")
# # else:
# #     print("Not equal")

# if s1.lower() == s2.lower():
#     print("Equal")
# else:
#     print("Not equal")

### Reverse String:

print(s1[::-1])
print(s1.title())
print(s1.split())
print("".join(s1))

print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

print(s1.find('a'))
print(s1.rfind('a'))
print(s1.count('a'))

print(s1.replace('a','b'))
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())
print(s1.capitalize())
