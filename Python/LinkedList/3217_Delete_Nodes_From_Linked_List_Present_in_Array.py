class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        while curr is not None:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
