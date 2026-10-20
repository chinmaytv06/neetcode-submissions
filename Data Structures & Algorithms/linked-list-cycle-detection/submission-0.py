# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cn = head
        d = set()

        while(cn != None):
            if cn in d:
                return True
            d.add(cn)
            cn = cn.next
        return False