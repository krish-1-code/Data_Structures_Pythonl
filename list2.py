#Indexing and Slicing 

#Items in the list are indexed just like how elements in the array are indexed

list1 = [1,2,3,4,5,6,7]

for items in list1:
    print(items)

list1[1] = 9

print(list1)

print(list1[::-1]) #for reverse


#List Packing and Unpacking:

numbers = [1,2,3,4]

first, second, third, fourth = numbers #This is unpacking

print(first)

first, second , *other = numbers

print(other)


#Count the frequency of char is a list.

#list1= ['a','a','b','z','d','z','z','d','i']

list1 = [1,2,2,3,4,1,2,3]
new = {}

for items in list1:
    if items not in new:
        new[items] = 0
    new[items] += 1

#for number, count in new.iteritems():
 #   pass

print(new)