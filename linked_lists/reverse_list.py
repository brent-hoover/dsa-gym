from node import Node

def reverse_list(head: Node):
    current = head
    prev = None
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev