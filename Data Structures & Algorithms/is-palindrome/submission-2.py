import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
       
        #replace white spaces
        s = s.replace(" ", "")
        #make lowercase
        s = s.lower()
        #filter out non alpha-numeric
        s = "".join(filter(str.isalnum, s))
        print(s)

        #second pointer
        end = len(s)-1

        for i in range (0, len(s)//2):
            print(s[i] + s[end])
            if s[i] == s[end]:
                end = end -1
                continue
            else:
                return False
                
        return True
