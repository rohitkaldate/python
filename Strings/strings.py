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


n=input("Enter string: ")
op=n[0].upper()+n[1:len(n)-1].lower()+n[-1].upper()
print(op)