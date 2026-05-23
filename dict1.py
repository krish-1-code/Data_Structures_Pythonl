#Count the frequency of char is a list.

#list1= ['a','a','b','z','d','z','z','d','i']

list1 = [1,2,2,3,4,1,2,3]
new = {} #Empty dict

for items in list1:
    if items not in new:
        new[items] = 0
    new[items] += 1

#for number, count in new.iteritems():
 #   pass

for keys, values in new.items():
    print(f"{keys} : {values}")