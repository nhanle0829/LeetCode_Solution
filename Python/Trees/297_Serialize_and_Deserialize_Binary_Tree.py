class Codec:

    def serialize(self, root):
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            root = queue.popleft()
            if root:
                res.append(str(root.val))
                queue.append(root.left)
                queue.append(root.right)
            else:
                res.append("N")
        return ",".join(res)

    def deserialize(self, data):
        if data == "N":
            return None

        data = data.split(",")
        root = TreeNode(data[0])
        i = 1
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if i < len(data) and data[i] != "N":
                curr.left = TreeNode(int(data[i]))
                queue.append(curr.left)
            if i + 1 < len(data) and data[i + 1] != "N":
                curr.right = TreeNode(int(data[i + 1]))
                queue.append(curr.right)
            i += 2
        return root
