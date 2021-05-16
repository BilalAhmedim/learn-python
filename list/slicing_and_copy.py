my_number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# print all element
print(my_number[:])

# copy all element into one variable to another
new_variable = my_number[:]

# print new variable
print(new_variable)

# cheking new variable as a diffent list 
new_variable.append('new element')
print(new_variable)

# slicing
# print whole list excluding first 2 element
print(my_number[2:])

# print whole list excluding last 2 element
print(my_number[:-2])

# print first two element in the list
print(my_number[:2])

# print last two element in the list
print(my_number[-2:])

# print 3 element in between list
print(my_number[3:-3])