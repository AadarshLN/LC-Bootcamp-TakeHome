# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        i = 0
        j = len(temp)-1
        while i<j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        return True
