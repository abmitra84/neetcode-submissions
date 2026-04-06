class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            try:
                _ = counter[nums[i]]  # check if key exists
                counter[nums[i]] += 1
            except:
                counter[nums[i]] = 1 # new key initiate count at 1

        count_dict = {i+1:[] for i in range(len(nums))} # initialize count dict
        # attach original values to their counts as index
        for j,v in counter.items():
            count_dict[v].append(j)
        
        # travel the dictionary in reverse
        res = []
        for i in range(len(nums), 0, -1):
            if len(count_dict[i])>0:
                res.extend(count_dict[i])
            if len(res) == k:
                break
        return res