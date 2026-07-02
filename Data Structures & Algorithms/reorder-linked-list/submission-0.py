# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Count length
        i = 0
        currNode = head
        while currNode:
            currNode = currNode.next
            i += 1
        
        splitNum = i // 2
        
        # Step 2: Split into two halves
        counter = 0
        lastDef = head
        while lastDef:
            if counter == splitNum:
                revHead = lastDef.next
                lastDef.next = None      # cut connection
                break
            lastDef = lastDef.next
            counter += 1
        
        # Step 3: Reverse the second half
        prev = None
        while revHead:
            nnNode = revHead.next
            revHead.next = prev
            prev = revHead
            revHead = nnNode
        secondHalf = prev
        
        # Step 4: Merge two halves
        first, second = head, secondHalf
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        
           
