# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxwidth=0
        q=deque()
        q.append((root,0))
        while q:
            n=len(q)
            mini=q[0][1]
            first=0
            last=0
            for i in range(n):
                node,idx=q.popleft()
                curr=idx-mini
                if i==0:
                    first=curr
                if i==n-1:
                    last=curr
                if node.left:
                    q.append((node.left,2*curr+1))
                if node.right:
                    q.append((node.right,2*curr+2))
            maxwidth=max(maxwidth,last-first+1)
        return maxwidth