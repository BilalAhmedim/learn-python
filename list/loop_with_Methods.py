# using range function to genrate sequential numbers in a loop
for value in range(1, 5):
  print(value)

# create a list using range function
number = list(range(1,6))
print(number)

# Genrate only even number using range function
even_number = list(range(2,11,2))
print(even_number)

# genrate first 10 square root values using loop
squares = []
for values in range(1, 11):
  square = values**2
  squares.append(square)

print(squares)

# find minimum, maxmum, and sum of list
newlist = list(range(0,10))
print('Minimum number of list: '+str(min(newlist)))
print('Maximum number of list: '+ str(max(newlist)))
print('Sum of list: '+ str(sum(newlist)))