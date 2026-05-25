#Count the number of node in a link list

class linklist:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def search(Head,target):
    curr = Head
    while(curr):
        if curr.val == target:
            return True 
        else:
            curr = curr.next


def countnode(Head):
    curr = Head
    node = 0
    while(curr):
        node = node + 1
        curr = curr.next
    #print(f"Number of node = {node}")
    return node

def middle(Head):
    
    temp = Head
    node = countnode(Head)

    if node%2 != 0:
        term = node // 2
    else:
        return "Even node"
    
    for i in range(term):
        Head = Head.next

    value = Head.val

    return value

Head = linklist(1)
A = linklist(2)
Tail = linklist(3)

Head.next = A
A.next = Tail

count = countnode(Head)
print(f"Number of node: {count}")

result = search(Head,5)

if result:
    print("Found")
else:
    print("NOt Found")

mid = middle(Head)
print(f"The middle val is {mid}")