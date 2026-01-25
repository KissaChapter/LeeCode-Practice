# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法一
# 课程解法 https://www.bilibili.com/video/BV14v411n7DF?p=2&vd_source=f8769668e775cd9306cdc3bdc68f4aa6
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2;
        if l2 == None:
            return   l1;

        dummy = ListNode(0)     # 这里的dummy表示虚拟头结点，指向头结点的指针
        p = dummy   # 随循环向后移动的指针
        carry = 0   # 进位

        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry) % 10
            carry = ListNode(l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l2:
            while l2:
                p.next = ListNode(l2.val + carry) %10
                carry = (l2.val + carry) // 10
                p.next = l2.next
                p = p.next

        if l1:
            while l1:
                p.next = ListNode(l1.val + carry) %10
                carry = (l1.val + carry) // 10
                p.next = l1.next
                p = p.next

        if carry == 1:
                p.next = ListNode(1)

        return dummy.next


#方法二：官方解法
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val+l2.val >= 10:
            i = 1
        else:
            i = 0
        node1 = ListNode((l1.val+l2.val)%10)
        node = node1
        if l1.next!=None and l2.next!=None:
            while l1.next and l2.next:
                node.next = ListNode((l1.next.val+l2.next.val+i)%10)
                if l1.next.val+l2.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l1 = l1.next
                l2 = l2.next
                node = node.next
        if l1.next != None:
            while l1.next:
                node.next = ListNode((l1.next.val+i)%10)
                if l1.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l1 = l1.next
                node = node.next
        if l2.next != None:
            while l2.next:
                node.next = ListNode((l2.next.val+i)%10)
                if l2.next.val+i >= 10:
                    i = 1
                else:
                    i = 0
                l2 = l2.next
                node = node.next
        if i == 1:
            node.next = ListNode(1)
        return node1