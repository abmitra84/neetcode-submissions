class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Assumption: only one pair of i and j exists
        Expectation: return the answer with smallest index first
        """
        # Approach:
        # 1. make hashmap h of the list
        # 2. pick x[i], calculate r = t - x[i]
        # 3. if r in h, return index(i, h.index())
        # 4. else move i to i+1
        for i in range(len(nums)):
            r = target - nums[i]
            try:
                j = nums[i+1:].index(r)  # check if the residual exists in the list to make x[i] + x[j] = target
                return [i,i+j+1] # the reason for check from i+1 is to avoid cases of duplicate elements
            except:
                continue # Assuming every input list has one i and j => no default return needed

        return [-1, -1]

        