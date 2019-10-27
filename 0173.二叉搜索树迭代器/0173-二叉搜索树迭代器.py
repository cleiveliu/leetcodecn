# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        def h(root):
            if not root:
                return
            yield from h(root.left)
            yield root.val
            yield from h(root.right)
        self.cache = []
        self.gen = h(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            return self.cache.pop()
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.cache:
            return True
        try:
            v = next(self.gen)
            self.cache.append(v)
            return True
        except:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()