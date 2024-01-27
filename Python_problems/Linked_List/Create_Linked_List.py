class Node:
    def __init__(self,val):
        self.data = val
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("**** List is Empty ****")
            return 
        temp = self.head 
        while temp:
            print(f"{temp.data}",end = " -> ")
            temp = temp.next
        print("None")    

    def insert_at_last(self,val):
        
        NewNode = Node(val)
        
        if self.head is None:
            self.head = NewNode
            return 
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = NewNode 
        return temp 
    
    def insert_at_start(self,val):

        NewNode = Node(val)
        NewNode.next = self.head 
        self.head = NewNode
        return 
        
    def get_length(self):
        count = 0 
        temp = self.head 
        while temp:
            count += 1
            temp = temp.next
        print(count)
        return count    
       
    def insert_at_position(self,val,position):

        if (position < 1) or (self.get_length() < position):
            print(f"Position {position} not Correct")
            return 
        
        if position == 1 :
            new = Node(val)
            new.next = self.head 
            self.head = new 
            return 
        
        temp = self.head 
        count = 1
        NewNode = Node(val)

        while position != 0 :
            position -= 0 

            

if __name__ == "__main__":

    
    mylist = LinkedList()
    mylist.get_length()
    mylist.insert_at_last(16)
    mylist.display()
    mylist.insert_at_last(18)
    mylist.display()
    mylist.get_length()
    mylist.insert_at_last(19)
    mylist.display()
    mylist.insert_at_start(13)
    mylist.display()
    mylist.insert_at_start(14)
    mylist.display()
    mylist.get_length()
    mylist.insert_at_position(32,1)
    mylist.display()
    mylist.insert_at_position(3.5,12)
    mylist.display()