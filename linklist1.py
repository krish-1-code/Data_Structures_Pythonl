# Link list is an another Data structure

# It can either be singly link list or doubly link list

#There are two main things that a link list contains: values and address to next or previous link list.

#The |___| containing the value and address is called node.

#The first node is called Head and the last node points out to NULL.

# There will be a class named node that will conatin node.value and node.next or node.previous

# Where is linked list better?
# - dynamic sizing og link lists
# - Fast insertions and deletions
# - No need for contiguos memory allocation

#Disadvantages:
# - Slower accessing cuz no indexes:
# - Extra memory cuz values along with the address
# - Cache performance is worse


class node:
    def __init__(self,value,link = None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value)

    
Head = node(5)
A = node(6)
B = node(7)

Head.link = A
A.link = B

print(Head)

def display(Head):
    curr = Head
    while(curr != None):
        print(curr)
        curr = curr.link

display(Head)

def proper_display(Head):
    curr = Head
    elements = []

    while(curr):
        elements.append(str(curr.value))
        curr = curr.link

    print("->".join(elements))

proper_display(Head)