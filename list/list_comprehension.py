# list Comprehension
list = [value**2 for value in range(1,11)]
print(list)
# value**2 storing value
# for value in range(1, 11) <---- normal loop
# add all the value into the storage variable with operation value(**2) like list.apppend(value**2)

# genrate 1 to 20 using list comprehension
list1 = [value for value in range(1,21)]
print(list1)

# genrate 1 to 1000000 and juump 1000 using list comprehension
onem = [value for value in range(1, 1000000, 1000)]
print(onem)
print(len(onem))

# Generate odd number using list comprehension
odd = [oddn for oddn in range(1, 20, 2)]
print(odd)

# genrate multiples of 3, 3 to 30
multi = [value for value in range(3, 30, 3)]
print(multi)

# genrater cube first 10
cube = [value**3 for value in range(1, 11)]
print(cube)