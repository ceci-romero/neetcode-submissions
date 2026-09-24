class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        res = []
        count = 0
        for i in nums:
            print(i)
            print(val)
            if i != val:
                res.append(i)
                count = count + 1
        print(res)

        for i in range(0, len(nums)):
            nums.pop()
        print("nums:" + str(nums))
        for i in res:
            nums.append(i)
        print(nums)
        return count

