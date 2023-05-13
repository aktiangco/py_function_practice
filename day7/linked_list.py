# Activity: Create a Linked List
# *! To check: python3 day7/linked_list.py

# Implement a Linked List
class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference

# node1 = Node(5)
# print(node1.data)
# node2 = Node(11)
# node1.reference = node2
# print(node1.reference)

class LinkedList:
    def __init__(self, head=None):
        self.head = None
        
    # Traverse a Linked List
    def print_linked_list(self):
       # checks if the linked list is empty 
        if self.head is None: 
            print("The link list is empty")
        # If the linked list is not empty
        else:
            c_node = self.head #c_node (representing the current node) 
            while c_node is not None: #Use a while loop since we know the end condition
                print(c_node.data)
                c_node = c_node.reference # We do this so the reference of the node becomes the new current node
    
    # Add a Node to the Beginning of a Linked List            
    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

                
# linked_list1 = LinkedList()
# linked_list1.print_linked_list()

linked_list1 = LinkedList()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.print_linked_list()

