from LinkedList import Node, create, display

# Description:
"""
Merging two linked list which are sorted. The resultant LL has to be sorted as well. 

2 -> 8 -> 10 -> 15 -> 22 -> 23
4 -> 7 -> 12 -> 14

Algorithm:
1. Take pointers, first = head of the first LL
2. second = head of the second LL
3. Take pointer result = null and last = null (we need to compare the data of the first nodes of first and second head)
4. assign result = first/second, last = first, first/second = first.next; last.next = null
5. compare first.data and second.data, make the lowest as next in the last and make last.next = null
6. Repeat 5 until first.next and second.next = null
7. Insert the remaining nodes of first and second. 
"""


def merge(node1: Node, node2: Node):
    first = node1
    second = node2
    result = Node(-1)
    last = Node(-1)

    # initialise result
    if first.data < second.data:
        result = first
        last = first
        first = first.next

    else:
        result = second
        last = second
        second = second.next

    last.next = None # make last.next = None

    # loop through both the LLs
    while first is not None and second is not None:
        if first.data < second.data:
            last.next = first
            last = first
            first = first.next
        else:
            last.next = second
            last = second
            second = second.next
        last.next = None

    # Remaining Node
    while first is not None:
        last.next = first
        last = first
        first = first.next

    while second is not None:
        last.next = second
        last = second
        second = second.next

    display(result)


merge(create([2, 8, 10, 15, 22, 23]), create([4, 7, 12, 14, 16, 18, 28, 31, 32, 34]))
