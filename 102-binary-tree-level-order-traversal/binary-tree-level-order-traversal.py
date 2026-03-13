# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        if not root:
            return []
        # print(q)
        res = []
        while q:
            # curr = q.popleft()
            # if curr.left:
            #     q.apeend(curr.left)
            # if curr.right:
            #     q.append(curr.right)
            l =len(q)
            temp = []
            for i in range(l):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp)
        return res
            

        