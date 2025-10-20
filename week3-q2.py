# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        mid = head
        prev_mid = None
        while fast and fast.next:
            prev_mid = mid
            mid = mid.next
            fast = fast.next.next

        prev = None
        prev_mid = None

        while mid:
            tmp_mid = mid.next
            mid.next = prev
            prev = mid
            mid = tmp_mid

        while head or prev:
            tmp_head = head.next if head else None
            tmp_prev = prev.next if prev else None
            
            if head:
                head.next = prev
            if prev:
                prev.next = tmp_head
            prev = tmp_prev
            head = tmp_head    
