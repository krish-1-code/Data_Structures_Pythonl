#Lists are 1/4 collections datatype

#There can be list of pretty much everything

#List of number
num = [1,2,3,4,5]

#List of strings
str = ["abc","def","ghi"]

#List of booleans:
bol = [True, False, False, True]

#List of lists:
Lst = [[1,2],["Yes","No"],[True,False]]

#One list can contain multiple datatypes.


#To have a list of same element:

lst = ['A'] * 10
print(lst)

#To concatinate two different lists:

list1 = [1,2,3,4,5]
list2= [True,False,True,False]

list3 = list1 + list2

print(list3)

#To use the built in list function:

#Create a list of 1 - 50

nums = list(range(50)) #50 is exclusive
print(nums)

nums1 = list(range(1,100,10)) #Steps work as well
print(nums1)


#What happends when we pass a string to the list function:

chars = list("Krish Kushwaha")
print(chars) #Divides it into individual chars

print(ord('A')) #Two print Ascii value