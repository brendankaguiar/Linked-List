class Node:
    def __init__(self,data):                
        self.data=data                      
        self.next=None                      
class Linked_List:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def display(self):
        if self.head is None:
            print("The list is empty")
        cur_node=self.head
        while True:
            if cur_node is None:
                break
            print(cur_node.data)
            cur_node=cur_node.next
    
    def delete(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None
            

firstNode = Node("Brendan")
secondNode = Node("Aguiar")
linkedList = Linked_List()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.display()
linkedList.delete()
linkedList.display()
#adding another delete will cause an error on line 34