def two_sum(list1, target):

    dict1 = {}
    list2 = []
    for i in range(len(list1)):
        remain = target - list1[i]

        if remain in dict1:
            list2.append([dict1[remain], i])

        dict1[list1[i]] = i

    return list2

print(two_sum([1,2,3,4,5],6))