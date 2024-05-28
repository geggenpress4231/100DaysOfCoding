class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and insert the smaller value node into the merged list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes from either list1 or list2
        current.next = list1 if list1 is not None else list2

        return dummy.next