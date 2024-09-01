"""
Given 2 non-empty linked lists
add 2 numbers and return sum as LL
any digits > 9 should carry

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or carry:
            tempval1 = l1.val if l1 else 0
            tempval2 = l2.val if l2 else 0

            sum = tempval1 + tempval2 + carry
            carry = sum // 10
            newval = sum % 10

            current.next = ListNode(newval)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next