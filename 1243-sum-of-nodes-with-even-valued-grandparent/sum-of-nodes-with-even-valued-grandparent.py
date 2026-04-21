# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # implemnting a depth first search
        def dfs(node , parent , grand):
            if not node:
                return 0
            tot = 0
            if grand and grand %2 == 0:
                tot+=node.val
            tot += dfs(node.left , node.val ,parent)
            tot += dfs(node.right , node.val ,parent)
            return tot
        return dfs(root,None , None)
        