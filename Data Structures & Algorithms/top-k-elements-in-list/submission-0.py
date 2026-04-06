from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = sorted(counts.items(), key=lambda item: item[1], reverse=True) # -> List
        return [res[i][0] for i in range(k)]


        