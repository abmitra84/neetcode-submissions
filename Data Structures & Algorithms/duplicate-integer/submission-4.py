class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}

        for ele in nums:
            print(hash_dict)
            if hash_dict.get(str(ele)) != None:
                return True
            else: 
                hash_dict[str(ele)] = 'dummy'
        return False
        