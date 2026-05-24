#Easy1

#Sum of all even number in the list:

list1 = [1,2,3,4,5,6]
sum = 0
for num in list1:
    if(num%2==0):
        sum = sum + num
print(sum)

#Max number:
sample = list1[0]
for num in list1:
    if num >= sample:
        sample = num
print(sample)

#Count chars:

s = "banana"
chars = list(s)
count = {}
counter = 1
for char in chars:
    if char not in count:
        count.update({char : counter})
    else:
        count[char] += 1

for keys, values in count.items():
    print(f"{keys} : {values}")

#Remove Duplicates:

list1 = [1,2,2,3,1,4]
new_list = []
for items in list1:
    if items not in new_list:
        new_list.append(items)

print(new_list)