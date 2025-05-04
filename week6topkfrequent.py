from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       result=Counter(nums)
       counts=result.most_common(k)
       return [i for i, j in counts]
