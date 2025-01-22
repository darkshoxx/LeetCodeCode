from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        end_reached = False
        result = ListNode(None)
        while not end_reached:
            my_sum = l1.val + l2.val 
            digit = my_sum % 10
            carry = my_sum > 10
            result = ListNode(val=digit)
            return result
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.addTwoNumbers
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)