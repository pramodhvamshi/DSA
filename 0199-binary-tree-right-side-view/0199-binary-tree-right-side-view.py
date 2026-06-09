# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def func(node,level,ans):
            if node==None:
                return
            if level==len(ans):
                ans.append(node.val)
            func(node.right,level+1,ans)
            func(node.left,level+1,ans)
        ans=[]
        func(root,0,ans)
        return ans