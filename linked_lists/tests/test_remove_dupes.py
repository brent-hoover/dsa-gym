from ..node import Node
from ..practice import remove_duplicates


def test_remove_duplicates():
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

    l1 = create_list([1, 1, 2])
    assert list_to_array(remove_duplicates(l1)) == [1, 2]

    l2 = create_list([1, 1, 2, 3, 3])
    assert list_to_array(remove_duplicates(l2)) == [1, 2, 3]

    l3 = create_list([1, 1, 1])
    assert list_to_array(remove_duplicates(l3)) == [1]