class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    #bucket sort, have buckets, and the sort values into the buckets
    #number of buckets == lenght of array. 

    #the count is the key/index, the value is the the numbers that have that count
        size = len(nums)

        count = {}
        freq = [[] for i in range(len(nums) +1)] #creates an empty arraay with the specified number of empty arrays.

        #count hashmap just keeps count of the each num
        for n in nums:
            count[n]= 1 + count.get(n,0) # get and increase the count, if does not exist get 0 value

        #this for loop adjusts the frequencies, which correspone to the index, and the number that has that count. 
        for n, c in count.items():
            freq[c].append(n)

        res = []

        print(count)
        print(freq)
        for i in range(len(freq) -1,0,-1): #decrementing from the end of freq
            for n in freq[i]:
                res.append(n)
                if len(res) == k:  #we know there will be k number of elements, so we can stop when len res ==k
                    return res

    


