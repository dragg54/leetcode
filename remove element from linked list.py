class ListNode:
    def __init__(self, next = None, val = 0):
        self.val = val
        self.next = next

class Solution:
    def removeElement(self, head, val):
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next =nxt
            else:
                prev = curr
            curr = nxt
        return dummy.nxt
 