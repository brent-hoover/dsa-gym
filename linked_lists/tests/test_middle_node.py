from ..node import Node
from ..practice import find_middle_node

def test_find_middle():
   def create_list(values):
       if not values: return None
       head = Node(values[0])
       curr = head
       for val in values[1:]:
           curr.next = Node(val)
           curr = curr.next
       return head

   # Odd length
   l1 = create_list([1,2,3,4,5])
   assert find_middle_node(l1).val == 3

   # Even length (return second middle)
   l2 = create_list([1,2,3,4])
   assert find_middle_node(l2).val == 3

   # Single node
   l3 = create_list([1])
   assert find_middle_node(l3).val == 1

   # Empty list
   assert find_middle_node(None) is None