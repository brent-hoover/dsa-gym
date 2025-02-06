from ..node import Node
from ..practice import is_palindrome

def test_is_palindrome():
   def create_list(values):
       if not values: return None
       head = Node(values[0])
       curr = head
       for val in values[1:]:
           curr.next = Node(val)
           curr = curr.next
       return head

   assert is_palindrome(create_list([1,2,2,1])) == True
   assert is_palindrome(create_list([1,2,3,2,1])) == True
   assert is_palindrome(create_list([1,2])) == False
   assert is_palindrome(create_list([1])) == True
   assert is_palindrome(None) == True