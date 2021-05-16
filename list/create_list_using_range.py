# create list using range function
number = list(range(1,11))
print(number)

# create list using range function and convert to string only one element list
list = str(list(range(0,11)))
print(type(list))

# not to do this if you de than get error
list = list(str(range(0,11)))
print(list)