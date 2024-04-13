from LinkedList import create, display, Node

# Algorithm
"""
1. create new_node = Node(element)
2. current  = head
3. Check if the element is less than the first node, then make the element as head
4. while current.next != null and current.data < new_node.data < current.next.data
5. Insert after current 
"""


def insert_in_sorted_list(head: Node, element: int):
    current = head
    new_node = Node(element)
    if element < current.data:
        new_node.next = current
        head = new_node
    else:
        while current.next is not None:
            if current.data < new_node.data < current.next.data:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
        current.next = new_node
    display(head)


linked_list = create([3, 7, 9, 15, 20])
insert_in_sorted_list(linked_list, 2)
