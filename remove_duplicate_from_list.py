class Solution:
    def remove_duplicate(self, head):
        cur = head
        while cur:
            while cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head