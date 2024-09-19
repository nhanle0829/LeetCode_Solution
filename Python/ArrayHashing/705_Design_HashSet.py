class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_map = [ListNode(0) for i in range(10_000)]

    def add(self, key: int) -> None:
        hash_val = key % 10_000
        curr = self.hash_map[hash_val]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        hash_val = key % 10_000
        curr = self.hash_map[hash_val]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        hash_val = key % 10_000
        curr = self.hash_map[hash_val]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False
