class Solution:

    def encode(self, strs: List[str]) -> str:

        biggoword = ""
        for word in strs:
            size = len(word)

            delimeter = str(size) + "#"

            biggoword = biggoword + delimeter + word

        print(biggoword)
        return biggoword

    def decode(self, s: str) -> List[str]:
        words = []
        index = 0

        #how long do we loop for?
        while index < len(s):
        
        #had to get this section for the solution
            #first position we;re going to be at is an integer
            j = index 

            while s[j] != '#':  #just making sure the delimeter is there
                j += 1 

            length = int(s[index:j]) # start at i up to j, but not including j, should just be an int
            isolated_word = s[j+1 : j+1+length]  #exmaple 4#love, j is at '#', length is '4', 

            words.append(isolated_word)
            index = j +1+length #update the index to the end of the word

        return words


        


 
            



        return True
