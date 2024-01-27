class Node:
    def __init__(self,val):
        self.data = val 
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None


    def insert_at_last(self,val):
        NewNode = Node(val)
        if self.head is None:
            self.head = NewNode
            print("Inserted into Empty Linked List")
            return 
        
        temp = self.head 
        while temp.next:
            temp = temp.next 
        temp.next = NewNode 
        print("Inserted")
        return  temp       


    def display(self):

        if self.head is None:
            print("Linked List is Empty ")
            return 
        
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")    


if __name__ == "__main__":

    a = linked_list()
    a.insert_at_last(5)
    a.insert_at_last(15)
    a.insert_at_last(52)
    a.display()                  