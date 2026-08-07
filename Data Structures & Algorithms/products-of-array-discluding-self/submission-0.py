class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        output = []

        for i, n in enumerate(nums):
            for index, number in enumerate(nums):
                if i != index :  
                    product = product * nums[index]
            output.append(product)
            product = 1


        print (product)
        
        return output