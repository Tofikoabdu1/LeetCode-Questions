# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, target):
        total_paths = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        def dfs(node, current_sum):
            nonlocal total_paths
            if not node:
                return
            current_sum += node.val
            total_paths += prefix_count[current_sum - target]
            prefix_count[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            prefix_count[current_sum] -= 1

        dfs(root, 0)
        return total_paths