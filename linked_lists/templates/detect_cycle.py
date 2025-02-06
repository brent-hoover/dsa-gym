from ..node import Node

def has_cycle(head: Node) -> bool:
    """
    Detect if a linked list has a cycle.

    A linked list has a cycle when a node's next pointer points to a previous node,
    creating a loop in the list.

    Args:
        head: First node of linked list

    Returns:
        True if cycle exists, False otherwise

    Note:
        - Should solve in O(n) time and O(1) space
        - Use Floyd's cycle detection (fast/slow pointers)
    """
    pass