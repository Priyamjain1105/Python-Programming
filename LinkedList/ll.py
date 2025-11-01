class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
def printLL(head):
    temp = head
    while(temp!=None):
        print(temp.data)
        temp = temp.next
    

def take_input():
    value = int(input("Enter the value of Node:-"))
    head = None
    
    while(value != -1):
        newNode = Node(value)
        if(head == None):
            head = newNode
        else:
            head.next = newNode
            
        value = int(input("Enter the value of the node:-"))
    return head

def take_input2():
    value = int(input("Enter value:"))
    if(value == -1):
        return None
    head = Node(value)
    perv = head
    while(value!=-1):
        value = int(input("Enter value:"))
        temp = Node(value)
        perv.next = temp
        perv=temp
        
    return head
        

        
        
        
def arrtoLL(l):
    head = Node(l[0])
    perv = head
    for i in range(1,len(l)):
        temp =  Node(l[i])
        perv.next= temp
        perv = temp
        
    return head
        
    
        
  

newhead = take_input2()
printLL(newhead)