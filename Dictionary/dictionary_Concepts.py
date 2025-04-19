##Dictionary :: It is group of key value pairs, key must be uniques but values may not,indexing , slicing not allowed, it is mutable in nature, and also dynamic in nature

# d={
#     'name':'durga','age':50,'name':'Raja','age':30,'name':'Rohit','age':24
# }
# print(d)
# print(type(d))


##Creation of dictionary
# d={}
# print(type(d))

# # using dict function::
# l=[(10,'q'),(20,'b'),(30,'c')]
# d=dict(l)
# print(d)

## Access elements of the dict::
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d['Durga'])
# key=input("Enter key :")
# if key in d:
#     print(d[key])
# else:
#     print("Key not present")


## add/ update the data to the key:::d[key]=value
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# d["Rohit"]=500
# print(d)

##delete data from the dict::del(d[key]):::
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# del(d["Raja"],d["Raju"])
# print(d)

### WAP to enter name and marks into the dictionary:::
# n=int(input("Enter no os students: "))
# d={}
# for i in range(n):
#     name=input("Eneter name: ")
#     marks=int(input("Enter marks: "))
#     d[name]=marks
# print(d)

## Membership operator are only applicable for the keys and not for the values
## '+' and '*' are not applicable in the dictionary

## Functions in dictionary::
#len(d):
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(len(d))

##get(key): Access value of specified key using this method
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d.get('Rohit'))

##update():: Updates d1 by adding all elements of the d2
# d1={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# d2={'Raj':1001,'Puran':1002}
# d1.update(d2)
# print(d1)

#keys()::returns only keys from the dict::
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d.keys())

##values()::Returns only values from the dict::
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d.values())


#items():;returns items of the dict in the form of the tuple::
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# i=d.items().  orr print(d.items())
# for x in i:
#     print(x)

###WAP to get value from the given key by user
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# key=input("Enter key: ")
# if key in d:
#     print(d.get(key))
# else:
#     print("Key not present so default values for key is: ",d.get(key,'hi'))


##pop()::removes key and returns the value asscociated with that key
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d.pop('Raja'))

##popitem():: Removes random item from the dict
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d.popitem())

##clear()::Removes all elements of the dictionary
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# d.clear()
# print(d)

##setdefault(key,value)::
# d={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# print(d.setdefault('Rashi',100000))
# print(d)

##Aliasiung and cloning::

##aliasing::
# d1={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# d2=d1
# d1['Raj']=1000
# print(d2)


##cloning ::or copy()::
# d1={'Durga':10,'Raja':50,'Ram':30,'Rushi':40,'Rohit':100,'Raju':24}
# d2=d1.copy()
# d1['rashi']=120210
# print(d1)
# print(d2)
