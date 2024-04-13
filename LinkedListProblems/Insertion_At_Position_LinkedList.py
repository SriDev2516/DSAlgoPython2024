from LinkedList import create, display, Node

# Algorithm
"""
Assume p = the position at which element has to move
8 -> 6 -> 9 -> 7 -> 5
Suppose in the above example, we want to insert an element (20) at position 4, that 
means "20" will be placed after "7", so we need move 4-1 = 3 steps

Algorithm:
1. current = node
2. new_node = None(element)
3. for i in range(1, 3): current = current.next
4. new_node.next = current.next
5. current.next = new_node

"""


def insert_at_pos(head: Node, element: int, pos: int):
    current = head
    new_node = Node(element)
    for i in range(1, pos):
        if current.next is not None:
            current = current.next

        else:
            break
    new_node.next = current.next
    current.next = new_node
    display(head)


linked_list = create([8, 3, 9, 7, 6])
insert_at_pos(linked_list, 20, 1)

# Analysis:
"""
O(1) -> If inserted at position 1, i.e. after first element
O(n) -> Insertion happens other than position 1
"""