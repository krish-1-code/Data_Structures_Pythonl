list = ['a','b','c']

#To add element

list.append('d')
print(list)

list.insert(4,'e')
print(list)

list.extend(['e','f','g'])
print(list)

#To delete

list.remove('b')
print(list)

list.pop()
print(list)

del list[0:2]
print(list)

list.clear()


#To search

list1 = [1,2,3,4,5]

print(1 in list1)

print(list1.index(2))