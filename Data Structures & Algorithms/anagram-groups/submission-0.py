class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #hashmap, key is the counts, and value is the words
        #example: 1e,1a,1t : ['"tea", "ate"]

        result = defaultdict(list) #don't have to deal with edge case of count not exisiting

        for word in strs:
            count = [0] * 26 # a...z

            for character in word:
                # want to map 'a' ot index 0, and 'z' to index 25
                count[ord(character) - ord("a")] += 1 #subtracting the ascii value of a, ex for a 80-80 = 0
    #in python, lists cannot be keys, need a tuple instead
            result[tuple(count)].append(word)
        print(result)

        return result.values() #the values are the groups anangrams ;)

