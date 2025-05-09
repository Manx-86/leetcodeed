class Solution(object):
    def twoSum(self, numbers, target):
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement] + 1, i + 1]
            num_dict[num] = i  
