
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        retval=[]
        for st in strs:

            retval.append(str(len(st)) + '#' + st)

        return "".join(retval)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
     
        
        retval=[]
        l = 0
        while l < len(s):
            r = l + 1
            while r <  len(s) and s[r] != "#":
                r += 1
            curr_length = int(s[l : r])
            retval.append(s[r + 1 : r + 1 + curr_length])
            l = r + curr_length + 1
        return retval

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))