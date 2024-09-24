class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        retval=0
        
        vowels=('a','e','i','o','u')
        for i in range(left,right+1):
            
            if words[i][0] in vowels and words[i][len(words[i])-1] in vowels:
                retval+=1
        
        return retval