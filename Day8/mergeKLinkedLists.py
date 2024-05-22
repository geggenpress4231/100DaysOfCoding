# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
      def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []

     
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
          
            val, index, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

          
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next