from Node import Node


def create_linked_list(input_arr: []):
    head = Node(input_arr[0])
    node = head
    for i in range(1, len(input_arr)):
        new_node = Node(input_arr[i])
        node.next = new_node
        node = new_node
    return head


def display(node: Node):
    while node is not None:
        print(f"{node.data}", end="-> ")
        node = node.next


def reverse_linked_list(node: Node):
    if node is not None:
        reverse_linked_list(node.next)
        print(f"{node.data}", end=" -> ")


def counting_nodes_of_linkedlist(node: Node):
    count = 0
    while node is not None:
        count += 1
        node = node.next
    print(f"The number of nodes are: {count}")


def counting_using_recursion(node: Node):
    count = 0
    if node is None:
        return 0
    x = counting_using_recursion(node.next)
    return x + 1


def sum_of_all_elements(node: Node):
    result = 0
    if node is None:
        return 0
    return sum_of_all_elements(node.next) + node.data


def maximum_linkedlist(node: Node):
    x = -1
    if node is None:
        return 0
    x = maximum_linkedlist(node.next)
    if x > node.data:
        return x
    else:
        return node.data


def search(node, target):
    if node is None:
        return None
    if target == node.data:
        return True
    return search(node.next, target)


def move_target_to_head(previous, node, current):
    previous.next = current.next
    current.next = node
    display(current)


def improve_search(node: Node, target):
    current = node
    pos = 1
    previous = Node(0)
    while current is not None:
        if current.data == target:
            break
        else:
            previous = current
            current = current.next
            pos += 1
    move_target_to_head(previous, node, current)


