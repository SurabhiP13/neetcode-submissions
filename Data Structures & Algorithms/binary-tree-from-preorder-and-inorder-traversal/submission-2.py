# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        p=deque(preorder)
        size=len(preorder)
        lookup={v:i for i, v in enumerate(inorder)}

        def solve(start, end):
            if start>end:
                return
            val=p.popleft()
            root=TreeNode(val)
            mid=lookup[val]
            root.left=solve(start, mid-1)
            root.right=solve(mid+1, end)

            return root
        return solve(0, size-1)
        





        