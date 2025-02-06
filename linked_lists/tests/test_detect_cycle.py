from ..node import Node
from ..practice import has_cycle


def test_has_cycle():
    def create_cycle(values, pos):
        if not values:
            return None
        head = Node(values[0])
        curr = head
        nodes = [head]

        for val in values[1:]:
            curr.next = Node(val)
            curr = curr.next
            nodes.append(curr)

        if pos >= 0:
            curr.next = nodes[pos]
        return head

    # Test 1: Cycle exists
    assert has_cycle(create_cycle([3, 2, 0, -4], 1)) == True

    # Test 2: No cycle
    assert has_cycle(create_cycle([1, 2, 3, 4], -1)) == False

    # Test 3: Single node cycle
    assert has_cycle(create_cycle([1], 0)) == True

    # Test 4: Empty list
    assert has_cycle(None) == False