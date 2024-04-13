from Node import Node


def display_linkedlist(node: Node):
    if node is not None:
        print(f"{node.data}", end=" -> ")
        display_linkedlist(node.next)
