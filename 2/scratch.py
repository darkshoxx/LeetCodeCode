class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
    
a = ListNode(1)
b = ListNode(2,a)
print(ListNode(0))
print(a)
print(b)

def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

# test cases
t1 = list_to_LL([1, 2, 3, 4, 5])  #ListNode(val=1, next={ListNode(val=2, next={ListNode(val=3, next={ListNode(val=4, next={ListNode(val=5, next={None})})})})})
t2 = list_to_LL([1, 2])  #ListNode(val=1, next={ListNode(val=2, next={None})})
t3 = list_to_LL([])

# answers
print(reverseList(t1))
print(reverseList(t2))
print(reverseList(t3))