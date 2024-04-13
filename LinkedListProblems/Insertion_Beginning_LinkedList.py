from LinkedList import create, display
from Node import Node

# Description and Algorithm Steps
"""
1. Create a node = head
2. Create a new_node using the element
3. new_node.next = node
4. head = new_node
"""


def insert_element_at_the_beginning(node: Node, element: int):
    current = node
    new_node = Node(element)
    new_node.next = current
    node = new_node
    display(node)


linkedlist = create([1, 4, 7, 8, 9, 10])
insert_element_at_the_beginning(linkedlist, -1)

