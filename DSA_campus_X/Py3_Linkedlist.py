class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.numNodes = 0
        
    def __len__(self):
        return self.numNodes
        
    def insertHead(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
        self.numNodes += 1
        
    def traverse(self):
        elements = []
        curr = self.head
        while(curr):
            elements.append(str(curr.value))
            curr = curr.next
            
        print("->".join(elements))
        
    def InsertTail(self, value):
        newNode = Node(value)
        curr = self.head
        while(curr.next):
            curr = curr.next
            
        curr.next = newNode
        
        self.numNodes +=1
        
    def Search(self, target):
        curr = self.head
        while(curr):
            if(target == curr.value):
                return True
            curr = curr.next
        return False
        
    def insertAfter(self,target,value):
        newNode = Node(value)
        
        curr = self.head
        while(curr.value != target):
            curr = curr.next
        
        newNode.next = curr.next
        curr.next = newNode
        
        self.numNodes +=1
        
    def Empty(self):
        self.head = None
        self.numNodes = 0
        
    def deleteFront(self):
        self.head = self.head.next
        self.numNodes -= 1
        
    def deleteTail(self):
        
        curr = self.head
        
        while(curr.next.next):
            curr = curr.next
            
        curr.next = None
        self.numNodes -= 1


        
    def deletebyValue(self,target):
        
        curr = self.head
        
        while(target != curr.next.value):
            curr = curr.next
            
        curr.next = curr.next.next

        self.numNodes -= 1

    def Position(self,value):
        curr = self.head
        index = 0

        while(curr):
            if(curr.value == value):
                return f"Target found on {index} index"
            index += 1
            curr = curr.next
        
        return "Target is not in the linked list"
#Creating a Object LL

LL = LinkedList()
print(len(LL))

LL.insertHead(10)
LL.insertHead(20)
LL.insertHead(30)

print(len(LL))

print("LinkedList: ")
LL.traverse()

print("Adding from the Tail")
LL.InsertTail(0)
LL.InsertTail(-10)
LL.InsertTail(-20)
LL.InsertTail(-30)

LL.traverse()
print(len(LL))

print("Searching for a element")

target = -40

print(f"Is {target} in the linkedlist? : {LL.Search(target)}")

print("Insert After 0")

LL.insertAfter(0,value = -5)
LL.traverse()
print(len(LL))

#Emptying the linkedlist

#LL.Empty()
LL.traverse()
print(len(LL))

LL.deleteFront()
LL.deleteFront()
LL.deleteFront()
LL.traverse()

print("Deleting from Tail")
LL.deleteTail()
LL.deleteTail()
LL.traverse()

print("Deleting the Target")

LL.deletebyValue(-5)
LL.traverse()

print("Finding the index")

outcome  = LL.Position(-90)
print(outcome)

