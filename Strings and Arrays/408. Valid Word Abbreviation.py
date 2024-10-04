class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        j=0
        i=0
        while i<len(abbr) and j<len(word):
            if abbr[i].isdigit():
                temp=""
                if abbr[i]=="0":
                    return False
                while i<len(abbr) and abbr[i].isdigit():
                    temp+=abbr[i]
                    i+=1
                    
                #i+=1
                temp=int(temp)
                
                j+=temp
                

            elif abbr[i]!=word[j]:
                print(word[j:])
                print(abbr[i:])
                return False
            else:
                j+=1
                i+=1

        return i==len(abbr) and j==len(word)
