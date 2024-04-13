class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create(input_arr: input):
    head = Node(input_arr[0])
    node = head
    for i in range(1, len(input_arr)):
        new_node = Node(input_arr[i])
        node.next = new_node
        node = new_node
    display(head)
    return head


def display(node: Node):
    current = node
    while current is not None:
        print(f"{current.data}", end=" -> ")
        current = current.next
    print()
