# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        length = 0

        while(head != None ):
            length += 1
            head = head.next

        mid = length // 2 + 1

        head = l

        c = 0
        while (head != None):
            c+=1
            if c == mid:
                return head
            head = head.next
        return head