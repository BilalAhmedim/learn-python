# using range function to genrate sequential numbers in a loop
for value in range(1, 5):
  print(value)

# genrate first 10 square root values using loop
squares = []
for values in range(1, 11):
  square = values**2
  squares.append(square)

print(squares)


# loop with index number we need to use enumerate() method
array = list(str(x) for x in range(11))
for index, item in enumerate(array):
  print(f'{index} -> {item}')