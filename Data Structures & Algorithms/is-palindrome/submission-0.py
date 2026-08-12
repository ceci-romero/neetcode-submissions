import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
       
        #replace white spaces
        clean_s = s.replace(" ", "")
        clean_s = clean_s.lower()

        letters_s = "".join(filter(str.isalnum, clean_s))
        print(letters_s)
    
        # clean_s = clean_s.lower()

        # cleaner_s = re.findall(r'[a-z]*', clean_s)
        end = len(letters_s)-1
        # print(cleaner_s)

        for i in range (0, len(letters_s)//2):
            print(letters_s[i] + letters_s[end])
            if letters_s[i] == letters_s[end]:
                end = end -1
                continue
            else:
                return False
            
        
            # if letters_s[start] == letters_s[end]:
            #     end = end -1
            #     print(letters_s[start] + " " + letters_s[end])
            #     continue
            #     end = end -1
            # else:
            #     return False
                
        return True
