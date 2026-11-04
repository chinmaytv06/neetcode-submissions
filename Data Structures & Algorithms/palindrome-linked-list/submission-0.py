# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = head 
        a = []
        while(head != None):
            a.append(head.val)
            head = head.next
        z = a[::-1]
        
        if z == a:
            return True
        else:
            return False

