class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=[]
        if len(nums)==1:
            return nums[0]
        else:
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)+1):
                    curr=0
                    curr=sum(nums[i:j])
                    maxx.append(curr)
        if max(nums)>max(maxx):
            return max(nums)
        else:
            return max(maxx)
