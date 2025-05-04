class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        second_half = slow_ptr.next
        slow_ptr.next = None
        reversed_half = None
        while second_half:
            temp = second_half.next
            second_half.next = reversed_half
            reversed_half = second_half
            second_half = temp
        first_half = head
        second_half = reversed_half
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next, second_half.next = second_half, temp1
            first_half, second_half = temp1, temp2
