class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_to_copy = {None: None}
        node_curr = head
        while node_curr:
            node_to_copy[node_curr] = ListNode(node_curr.val)
            node_curr = node_curr.next

        node_curr = head
        while node_curr:
            copy = node_to_copy[node_curr]
            copy.next = node_to_copy[node_curr.next]
            copy.random = node_to_copy[node_curr.random]
            node_curr = node_curr.next

        return node_to_copy[head]
