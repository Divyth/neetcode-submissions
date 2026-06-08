# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        groups = n // k
        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy
        currStart = head

        for _ in range(groups):
            groupStart = groupPrev.next
            prev = None
            curr = groupStart

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            groupPrev.next = prev
            groupStart.next = curr

            groupPrev = groupStart
        return dummy.next

        
        