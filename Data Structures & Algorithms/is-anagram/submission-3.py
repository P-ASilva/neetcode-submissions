class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        index = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in index:
                    index[s[i]] += 1
                else:
                    index[s[i]] = 1

                if t[i] in index:
                    index[t[i]] -= 1
                else: 
                    index[t[i]] = -1

            for k, v in index.items():
                if v != 0:
                    return False
            return True
        return False
        