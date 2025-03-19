# Print * * *:

n=int(input("Enter number: "))
# for i in range(n):
#     print("* ",end=" ")

##Print pattern as
# * * *
# * * * :::

# for i in range(n):
#     print("* "*n)


## Print right angle triangle:

# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()


## Print inverted right angle triangle:

# for i in range(n):
#     print("* "*(n-i))


## Print pyramid pattern:

# for i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1))


## Print inverted pyramid:

for i in range(n):
    print(" "*i + "* "*(n-i))