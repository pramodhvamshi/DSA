#Space Optimization
class Solution:
    def func(self,nums):
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=prev2
            notPick=0+prev
            curi=max(pick,notPick)
            prev2=prev
            prev=curi
        return prev
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        temp=nums[1:]
        temp2=nums[:-1]
        return max(self.func(temp),self.func(temp2))