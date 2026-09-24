class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=nums[i]
            tot=0

            while x>0:
                tot+=x%10
                x//=10
            if tot==i:
                return i
        return -1