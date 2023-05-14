# Activity: Create a Linked List
# *! To check: python3 day7/linked_list.py

# Implement a Linked List
class Node:
    def __init__(self, data, reference=None):
        # Initialize a Node with data and a reference to the next Node
        self.data = data
        self.reference = reference

# node1 = Node(5)
# print(node1.data)
# node2 = Node(11)
# node1.reference = node2
# print(node1.reference)

class LinkedList:
    def __init__(self, head=None):
        # Initialize a Linked List with a head Node (default is None)
        self.head = None
        
    # Traverse a Linked List
    def print_linked_list(self):
        # Check if the linked list is empty
        if self.head is None: 
            print("The linked list is empty")
        # If the linked list is not empty
        else:
            c_node = self.head  # Assign the head Node to c_node (current node)
            while c_node is not None:  # Loop until the current node becomes None (end of the linked list)
                print(c_node.data)  # Print the data of the current node
                c_node = c_node.reference  # Move to the next node by updating c_node to its reference
    
    # Add a Node to the Beginning of a Linked List            
    def add_to_start(self, data):
        n_node = Node(data)  # Create a new Node with the given data
        n_node.reference = self.head  # Set the reference of the new node to the current head node
        self.head = n_node  # Update the head node to the new node, making it the new head
    
    def add_item(self, data):
        n_node = Node(data)
        if self.head is None:
            self.head = n_node
        else:
            c_node = self.head
            # Traverse the linked list until the last node
            while c_node.reference is not None:
                c_node = c_node.reference
            # Append the new node at the end of the linked list
            c_node.reference = n_node

    def add_item_after(self, data, value):
        n_node = Node(data)
        if self.head is None:
            raise ValueError("The linked list is empty")
        else:
            c_node = self.head
            # Traverse the linked list to find the node with the specified value
            while c_node is not None:
                if c_node.data == value:
                    # Insert the new node after the node with the specified value
                    n_node.reference = c_node.reference
                    c_node.reference = n_node
                    return
                c_node = c_node.reference
        raise ValueError("Value not found in the linked list")

    def remove_item(self, value):
        if self.head is None:
            raise ValueError("The linked list is empty")
        elif self.head.data == value:
            # Remove the head node if it contains the specified value
            self.head = self.head.reference
        else:
            c_node = self.head
            # Traverse the linked list to find the node with the specified value
            while c_node.reference is not None:
                if c_node.reference.data == value:
                    # Remove the node with the specified value by updating references
                    c_node.reference = c_node.reference.reference
                    return
                c_node = c_node.reference
        raise ValueError("Value not found in the linked list")            
    
# linked_list1 = LinkedList()
# linked_list1.print_linked_list()

linked_list1 = LinkedList()  # Create a new LinkedList object
linked_list1.add_to_start(82)  # Add node with data 82 to the beginning of the linked list
linked_list1.add_to_start(15)  # Add node with data 15 to the beginning of the linked list
linked_list1.add_item(33)  # Add node with data 33 to the end of the linked list
linked_list1.add_item_after(45, 15)
# Add node with data 45 after the first occurrence of the node with data 15 in the linked list
linked_list1.remove_item(82)  # Remove the first occurrence of the node with data 82 from the linked list
linked_list1.print_linked_list()  # Print the elements in the linked list
