class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num_dict = {}

        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 0
            else:
                num_dict[num] += 1

        print(num_dict)
        
        result = 0

        for key in num_dict:
            print(key)
            if num_dict[key] == 0:
                continue;
            else:
                return True
        
        return False

        
        