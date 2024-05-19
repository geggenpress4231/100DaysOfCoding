
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        head2 = slow.next
        slow.next = None  # Split the list into two halves
        head2 = self.reverseList(head2)
        
        # Step 3: Merge the two halves
        self.mergeLists(head, head2)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> None:
        while l1 and l2:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            if not l1_next:  # End of the first half
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next