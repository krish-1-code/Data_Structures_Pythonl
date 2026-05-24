#from linklist2 import singlelink, traversal


class singlelink:
    def __init__(self,val,link = None):
        self.val = val
        self.link = link

    def __str__(self):
        return str(self.val)

Head = singlelink(2)
A = singlelink(4)
B = singlelink(6)
C = singlelink(8)

Head.link = A
A.link = B
B.link = C

def insert_front(Head, value):
    curr = Head
    new_node = singlelink(value)
    new_node.link = curr
    return new_node

newlist = insert_front(Head,1)

def traversal(List):
    curr = List
    elements = []
    while(curr):
        elements.append(str(curr.val))
        curr = curr.link

    print("->".join(elements))

traversal(newlist)        
