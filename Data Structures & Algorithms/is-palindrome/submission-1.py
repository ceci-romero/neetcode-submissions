import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
       
        #replace white spaces
        clean_s = s.replace(" ", "")
        #make lowercase
        clean_s = clean_s.lower()
        #filter out non alpha-numeric
        letters_s = "".join(filter(str.isalnum, clean_s))
        print(letters_s)

        #second pointer
        end = len(letters_s)-1

        for i in range (0, len(letters_s)//2):
            print(letters_s[i] + letters_s[end])
            if letters_s[i] == letters_s[end]:
                end = end -1
                continue
            else:
                return False
                
        return True
