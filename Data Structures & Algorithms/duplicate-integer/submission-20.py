class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique_nums = {} 
        for num in nums:
            if num in unique_nums.keys():
                unique_nums[num] += 1
            else:
                unique_nums[num] = 1
        
        print(unique_nums)

        res = 0
        for num in nums:
            if unique_nums[num] > 1:
                print(unique_nums[num])
                return True

        

        return False

