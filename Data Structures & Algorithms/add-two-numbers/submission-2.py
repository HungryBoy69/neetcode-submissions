class Solution:
    def getReverseLinkedList(self, head):
        prev, curr = None, head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head1 = self.getReverseLinkedList(l1)
        # head2 = self.getReverseLinkedList(l2)
        head1 , head2 = l1, l2
        dummy = ListNode()
        tail = dummy
        carry = 0
        print(head1.val, head2.val)
        while head1 or head2 or carry:
            num1 = head1.val if head1 else 0
            num2 = head2.val if head2 else 0
            total = num1 + num2 + carry
            print(total, 'total')
            carry, remainder = divmod(total, 10)
            print(carry, remainder, 'carry')
            tail.next = ListNode(remainder)
            tail = tail.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        return dummy.next
