# Declare Empty List
list = ['0','1', '35', '449', '0']

# insert Method
list.insert(0,'2') # insert 2 at location of 0 in the list

# Modify list
list[0] = '1'

# insert item using append method at the last of the list
# apppend metho use to add item at end of the list
list.append('2')

# delete item using pop
poped = list.pop()
print('poped item: '+ str(poped))

# delete item using del keyword
del list[0]

# delete element using remoev method
list.remove('1') # in this method you need to know the element to delete not the location

# sorting temporary
print(sorted(list)) # this metho is temporary sort list

# sorting permanent
list.sort()

# final out put with length of list
print('Final Output: '+ str(list) +'\nlist length is: ' + str(len(list)))

