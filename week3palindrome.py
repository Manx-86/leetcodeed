class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_ptr = fast_ptr = head
        val_stack = []
        while fast_ptr and fast_ptr.next:
            val_stack.append(slow_ptr.val)
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr:
            slow_ptr = slow_ptr.next
        while slow_ptr:
            if val_stack.pop() != slow_ptr.val:
                return False
            slow_ptr = slow_ptr.next
        return True
