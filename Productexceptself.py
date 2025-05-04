class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        lisk=[]

        if 0 not in nums:
            for i in nums:
                prod*=i
            for t in nums:
                lisk.append(int(prod/t))
        elif nums.count(0)==2:
            for t in nums:
                lisk.append(0)
        else:
            kk=nums.index(0)
            nums.remove(0)
            for i in range(len(nums)):
                prod*=nums[i]
            for i in nums:
                lisk.append(0)
            lisk.insert(kk,prod)
        return lisk
    
        
