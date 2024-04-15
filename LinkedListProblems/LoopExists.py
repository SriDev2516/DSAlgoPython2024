from LinkedList import Node, create, display

# Description
"""
Find if a loop exists in a Linked List. 

Approach: 
If two pointer move in a straight line with different speeds, they will never intersect
But, if we make them move in circular path with different speed, they will intersect

The above concept is used to find the loop in the linked list. 

Algorithm:
1. Take Q1 and Q2
2. Q1 => head.next
3. Q2 => head.next.next // Check for Q2.next == None and then assign
4. If Q1 || Q2 == None => No loop exists and LL is linear
5. If Q1 == Q2 => Loop exists


"""


def loop_exists(node: Node):
    q1 = node
    q2 = node

    while q1 is not None and q2 is not None:
        q1 = q1.next
        if q2.next is None:
            return False
        else:
            q2 = q2.next.next

        if q1 == q2:
            return True

    return False


def create_loop(node: Node):
    t1 = node.next.next
    t2 = node.next.next.next.next
    t2.next = t1
    return node


print(loop_exists(create_loop(create([10, 20, 30, 40, 50]))))