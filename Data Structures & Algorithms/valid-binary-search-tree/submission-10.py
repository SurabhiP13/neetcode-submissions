# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, root, mini, maxi):
        if root.val>mini and root.val<maxi:
            if not root.left and not root.right:
                return True
            if root.left and root.right:
                return self.valid(root.left, mini, root.val) and self.valid(root.right, root.val, maxi)
            if not root.left and root.right:
                return self.valid(root.right, root.val, maxi)
            if root.left and not root.right:
                return self.valid(root.left, mini, root.val)
        else:
            return False
              

        

        

    
