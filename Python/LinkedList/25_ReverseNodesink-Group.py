class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            nth = self.get_nth_node(group_prev, k)
            if not nth:
                break

            group_next = nth.next
            curr, prev = group_prev.next, nth.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = nth
            group_prev = temp
        return dummy.next

    def get_nth_node(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node