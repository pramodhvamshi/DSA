class Solution:
    def maxIndex(self,mat,col):
        m=len(mat) 
        n=len(mat[0]) 
        ind=0
        mx=0
        for i in range(m):
            if(mat[i][col]>mx):
                mx=mat[i][col]
                ind=i
        return ind
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat) 
        n=len(mat[0]) 
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2 
            row=self.maxIndex(mat,mid) 
            if(mid-1>=0):
                left=mat[row][mid-1]
            else:
                left=-1
            if(mid+1<=n-1):
                right=mat[row][mid+1]
            else:
                right=-1
            if(mat[row][mid]>left and mat[row][mid]>right):
                return [row,mid]
            elif(left>mat[row][mid]):
                high=mid-1
            else:
                low=mid+1