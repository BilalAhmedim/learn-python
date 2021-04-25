# pre-defined list
items = ['Element one', 'Element two', 'Element tree', 'Element n']

# first we create item to store all items from old list one by one
# item[0] = items[0]
# item[1] = items[1]
# item[2] = items[2]
# item[n] = items[n]
for item in items:
  print(item)

msg = 'this is item from items: '
for item in items:
  print( (msg + item).title() )