class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
def ill():
    value = int(input("Enter New Data"))
    head = Node(value)
    perv = head
    
    while(value != -1):
        value = int(input("Enter New Value"))
        temp = Node(value)
        perv.next = temp
        perv=temp
        
    return head

def printLL(head):
    temp = head
    while(temp.next!=None):
        print(temp.data,"->",end="")
        temp = temp.next
        
        
def run():
    head = ill()
    printLL(head)
    
run()