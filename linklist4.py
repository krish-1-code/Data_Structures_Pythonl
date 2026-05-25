#This is the final link list file: Here we'll be practising:

# 1. Creating single / double link list
#2. Traversing the link list
#3. Finding the target
#4. Adding node to the front and the end
#5 Deleting node: first - last - and specific

class doublelink:
    def __init__(self, val, next = None, prev = None):
        self.val  = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)

def traversal(Head):
    curr = Head
    items = []
    while(curr):
        items.append(str(curr.val))
        curr = curr.next
    print("<->".join(items))

def backtraversal(tail):
    curr = tail
    items = []

    while(curr):
        items.append(str(curr.val))
        curr = curr.prev

    print("<->".join(items))

def find(Head,target):
    curr = Head

    while(curr):
        if curr.val == target:
            return True
        else:
            curr = curr.next

def addfront(Head,value):

    temp = Head
    new_item = doublelink(value)

    new_item.next = temp #doesn't affect the original link list

    return new_item

def addback(Head,value):

    temp = Head
    new_node = doublelink(value)

    while(temp.next):
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp #Affects the original link list
    return new_node

def deletefront(Head):

    temp = Head
    Head = temp.next

    traversal(Head)

def deletelast(Head):
    temp = Head

    while(temp.next.next):
        temp = temp.next

    temp.next = None

    traversal(Head)

Head = doublelink(5)
Body = doublelink(10)
Tail = doublelink(15)

Head.next = Body
Body.prev = Head
Body.next = Tail
Tail.prev = Body

traversal(Head)
backtraversal(Tail)

#search = int(input("Enter the target: "))

#result = find(Head, search)
#if result:
#    print("Target found")
#else:
#    print("Target didn't found")

add1 = int(input("What do you wanna add to the front: "))

NewHead = addfront(Head,add1)

add2 = int(input("What do you wanna add to the end: "))

NewTail = addback(Head,add2)

traversal(NewHead)
backtraversal(NewTail)
traversal(Head)
deletefront(Head)
deletelast(Head)