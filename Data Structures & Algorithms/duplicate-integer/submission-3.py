class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_sorted = sorted(nums) # extra O(n)
        nums.sort() # <- extra space to O(1)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            else:
                continue
        return False