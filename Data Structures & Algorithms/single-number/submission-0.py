class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_check = {}

        for n in nums:
            if n in number_check.keys():
                #add 1 to keys
                number_check[n] = 2
            else:
                number_check[n] = 1
        
        for key in number_check.keys():
            if number_check[key] == 1:
                return key
