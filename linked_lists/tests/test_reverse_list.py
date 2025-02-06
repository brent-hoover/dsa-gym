import pytest
from ..node import Node
from reverse_list import reverse_list


def test_reverse_list_basic():
    # Create: 1->2->3
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = reverse_list(head)

    # Check: 3->2->1
    assert result.val == 3
    assert result.next.val == 2
    assert result.next.next.val == 1
    assert result.next.next.next is None


def test_reverse_list_single():
    head = Node(1)
    result = reverse_list(head)
    assert result.val == 1
    assert result.next is None


def test_reverse_list_empty():
    assert reverse_list(None) is None