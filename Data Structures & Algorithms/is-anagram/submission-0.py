class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        dictionary_s = {} # key is character, value is the count
        dictionary_t = {}

        for index, i in enumerate(s):
            if i in dictionary_s:
                dictionary_s[i] = dictionary_s[i] + 1
            else:
                dictionary_s[i] = 1
        
        for index, i in enumerate(t):
            if i in dictionary_t:
                dictionary_t[i] = dictionary_t[i] + 1
            else:
                dictionary_t[i] = 1

        for c in dictionary_s:
            print(dictionary_s)
            print(dictionary_t)
            if c not in dictionary_t:
                return False
                
            if dictionary_s[c] != dictionary_t[c]:
                return False
          
        
        return True


        


            

    

    