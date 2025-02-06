from ..node import Node
from ..practice import remove_nth_from_end


def test_remove_nth_from_end():
    def create_list(values):
        if not values: return None
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

    # Remove 2nd to last
    l1 = create_list([1, 2, 3, 4, 5])
    assert list_to_array(remove_nth_from_end(l1, 2)) == [1, 2, 3, 5]

    # Remove first
    l2 = create_list([1, 2, 3])
    assert list_to_array(remove_nth_from_end(l2, 3)) == [2, 3]

    # Remove last
    l3 = create_list([1, 2, 3])
    assert list_to_array(remove_nth_from_end(l3, 1)) == [1, 2]

    # Single node
    l4 = create_list([1])
    assert remove_nth_from_end(l4, 1) is None