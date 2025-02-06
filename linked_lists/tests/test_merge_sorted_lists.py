import pytest
from ..node import Node
from ..practice import merge_sorted_lists


def test_merge_sorted_lists():
    """
    Merge Two Sorted Linked Lists

    Given two sorted linked lists l1 and l2, merge them into a single sorted linked list.
    Both input lists are sorted in ascending order. Return the head of the merged list.

    Args:
       l1: Head of first sorted linked list
       l2: Head of second sorted linked list

    Returns:
       Head of merged sorted linked list

    Notes:
       - Lists are already sorted in ascending order
       - You can create new nodes (doesn't need to be in-place)
       - Need to handle cases where lists are different lengths
       - Need to handle cases where one or both lists are empty
    """
    def create_list(values):
        if not values:
            return None
        head = Node(values[0])
        curr = head
        for val in values[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head

    def list_to_array(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test 1: Basic merge
    l1 = create_list([1, 3, 5])
    l2 = create_list([2, 4, 6])
    assert list_to_array(merge_sorted_lists(l1, l2)) == [1, 2, 3, 4, 5, 6]

    # Test 2: Lists of different lengths
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4, 5, 6])
    assert list_to_array(merge_sorted_lists(l1, l2)) == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test 3: One empty list
    assert list_to_array(merge_sorted_lists(None, create_list([1, 2, 3]))) == [1, 2, 3]

    # Test 4: Both empty lists
    assert merge_sorted_lists(None, None) is None