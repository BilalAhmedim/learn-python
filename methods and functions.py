import random

# create a list using range function
number = list(range(1,6))
print(number)

# Genrate only even number using range function
even_number = list(range(2,11,2))
print(even_number)

# find minimum, maxmum, and sum of list
newlist = list(range(0,10))
print('Minimum number of list: '+str(min(newlist)))
print('Maximum number of list: '+ str(max(newlist)))
print('Sum of list: '+ str(sum(newlist)))

# random.choice method
array = list(str(x) for x in range(11))
print(f'random number genrated in array is {random.choice(array)}')
random.shuffle(array)
print(f'shuffled array is {array}')

# get index value using value of list after shuffle
print(array.index('5'))
