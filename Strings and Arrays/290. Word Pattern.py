class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        hm={}
        p=list(pattern)
        s=s.split(" ")
        if len(s)!=len(p):
            return False

        st=set()
        for i,j in zip(p,s):

            if i not in hm :
                if j in st:
                    return False
                hm[i]=j
                st.add(j)

            elif hm[i]!=j:
                return False

        return True