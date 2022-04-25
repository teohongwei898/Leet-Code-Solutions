# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse 2nd half
        second = slow.next
        prev = slow.next = None
        while second:  #change direction
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge
        first, second = head, prev
        while second:
            temp1,temp2=first.next,second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
