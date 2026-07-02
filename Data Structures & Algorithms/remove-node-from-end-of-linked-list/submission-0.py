# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0 
        cur = head
        while cur:
            cur= cur.next
            N+=1
        removeIndex = N - n
        if removeIndex == 0:
            return head.next
        prev, cur = None, head
        i = 0
        while cur:
            if i == removeIndex:
                newNode = cur.next
                prev.next = newNode
                cur.next = None
                break
            prev = cur
            cur = cur.next
            i+=1
        return head
