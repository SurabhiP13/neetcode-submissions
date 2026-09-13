# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        self.solve(root, res, 0)
        return res

    
    def solve(self, root,res, counter):
        if not root:
            return None
        if counter < len(res) and res[counter]:
            res[counter].append(root.val)
        else:
            res.append([root.val])
        counter += 1
        self.solve(root.left, res, counter)
        self.solve(root.right, res, counter)



        

        
        

        
        
