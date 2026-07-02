class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 , head2 = l1, l2
        dummy = ListNode()
        tail = dummy
        carry = 0
        print(head1.val, head2.val)
        while head1 or head2 or carry:
            num1 = head1.val if head1 else 0
            num2 = head2.val if head2 else 0
            total = num1 + num2 + carry
            carry, remainder = divmod(total, 10)
            tail.next = ListNode(remainder)
            tail = tail.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        return dummy.next
