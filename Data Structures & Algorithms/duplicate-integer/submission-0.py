class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_nums = {}

        for index, num in enumerate(nums):

            if ( num in unique_nums):
                return True
            else: 
                unique_nums[num] = num
        
        return False


         