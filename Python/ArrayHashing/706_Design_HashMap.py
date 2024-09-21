class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash_map = [ListNode(0, 0) for i in range(1_000)]

    def put(self, key: int, value: int) -> None:
        hash_val = key % 1_000
        curr = self.hash_map[hash_val]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hash_val = key % 1_000
        curr = self.hash_map[hash_val]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash_val = key % 1_000
        curr = self.hash_map[hash_val]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
