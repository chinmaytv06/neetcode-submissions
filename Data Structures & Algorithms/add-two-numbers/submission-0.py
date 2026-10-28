# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l = l1
        # a=0
        # b=0
        # while(l1!=None):
        #     a=a*10
        #     a+=(l1.val)
        #     l1 = l1.next
        
        # while(l2 != None):
        #     b=b*10
        #     b+=(l2.val)
        #     l2= l2.next

        # x = a+b

        # l3 = []
        # while(x!=0):
        #     r = x%10
        #     x = x//10
        #     l3.append(r)
        # l1=l
        # i=0
        # while(l1!=None):
        #     l1.val = l3[i]
        #     i+=1
        #     l1=l1.next
        # l1 = l
        # return l1
        
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        
        
