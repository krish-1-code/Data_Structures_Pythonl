#In this code we will be creating a linklist, traversing it, and search for a value

class singlelink:

    def __init__(self, value, link = None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value)
    
Head = singlelink(5)
A = singlelink(10)
B = singlelink(15)
C = singlelink(20)

Head.link = A
A.link = B
B.link = C

#Traversing the link list:

def traversal(Head):
    curr = Head
    items = []

    while(curr):
        items.append(str(curr.value))
        curr = curr.link

    print("->".join(items))


if __name__ == "__main__":
    target = int(input("Which element do you wanna locate: "))
    traversal(Head)


def find(head, target):
    curr = head

    while(curr):
        if curr.value == target:
            return 1
        else:
            curr = curr.link

    return 0

result = find(Head, target)

if result == 1:
    print("Target found")
else:
    print("Target not found")

