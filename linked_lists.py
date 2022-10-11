class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self, data):
        new_node = Node(data, self.head)
        new_node.next = self.head
        self.head = new_node
        
    def print_linked_list(self):
        if self.head is None:
            print('Linked List is empty!')
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end = " ")
                n = n.next
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
                
LL1 = LinkedList()
LL1.insert_at_begin(9)
LL1.insert_at_begin(100)
LL1.insert_at_end(5)
LL1.insert_at_end(34)
LL1.print_linked_list()
        
