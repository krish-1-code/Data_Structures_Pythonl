
#REAPLCE MAXIMUM ITEMS OF THE LINKEDLIST WITH THE GIVEN VALUE:

class Node:
    def __init__(self,value,next =None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.num = 0

    def __len__(self):
        return self.num

    def append(self,value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode

        else:
            curr = self.head

            while(curr.next):
                curr = curr.next

            curr.next = newNode

    def traverse(self):
        elements = []
        temp = self.head

        while(temp):

            elements.append(str(temp.value))
            temp = temp.next

        print("->".join(elements))

    def replaceMax(self,value):

        newNode = Node(value)

        if self.head == None:
            return "Empty LinkedList"
       
        curr = self.head
        max = curr.value

        while(curr):
            if(max < curr.value):
                max = curr.value
            curr = curr.next

        curr = self.head
       

        while(curr.value != max):
            curr = curr.next

       
        curr.value = value



LL = LinkedList()
LL.append(10)
LL.append(20)
LL.append(50)
LL.append(30)

LL.traverse()


print("replacing the max value with 0")
LL.replaceMax(0)
LL.traverse()