class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache={}
        
        def dfs(sentence,wordDict):
            if not sentence:
                return True
            if sentence in cache:
                return cache[sentence]

            for end in range(len(sentence)+1):

                prefix=sentence[:end]

                if prefix in wordDict:
                    if dfs(sentence[end:],wordDict):
                        cache[sentence]=True
                        return True
            cache[sentence]=False
            return cache[sentence]
        
        return dfs(s,wordDict)