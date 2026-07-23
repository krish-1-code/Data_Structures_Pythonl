import sys

list1 = []

for i in range(1,11):
    print(i, sys.getsizeof(list1))
    list1.append(i)
    