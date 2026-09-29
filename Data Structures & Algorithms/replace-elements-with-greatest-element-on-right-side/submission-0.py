class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:


        for i in range(0, len(arr)):
            if i != (len(arr)-1):
                temp = arr[i+1:]
                print(temp)
                n = max(temp)
                arr[i] = n
            else:
                n = -1
                arr[i] = n
            temp = []

            print(n)
                

        return arr