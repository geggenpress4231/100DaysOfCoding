class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
      
        for _ in range(n + 1):
            right = right.next
        
       
        while right:
            left = left.next
            right = right.next
        
        
        left.next = left.next.next
        
    
        return dummy.next
