class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  #Create linked list with ListNode()
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val >= list2.val:
            head.val = list2.val
            head.next = self.mergeTwoLists(list1,list2.next)      #Iteration, use self.FunctionName!
        else:
            head.val = list1.val
            head.next = self.mergeTwoLists(list1.next,list2)
            
        return head
        
