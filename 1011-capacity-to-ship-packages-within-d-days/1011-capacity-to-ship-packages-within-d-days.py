class Solution:
    def func(self, weights: List[int], cap: int) -> int:
        dayss=1
        load=0
        n=len(weights)
        for i in range(n):
            if load+weights[i]>cap:
                dayss=dayss+1
                load=weights[i]
            else:
                load=load+weights[i]
        return dayss

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            if self.func(weights,mid)<=days:
                high=mid-1
            else:
                low=mid+1
        return low
        