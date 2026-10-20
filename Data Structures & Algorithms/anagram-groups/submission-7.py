class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep a dict for each anagram; create a new one for a non-match.
        # upon first match f the anagram, add initial and current to dict, them just current
        # anagrams need same len, keep a len intro on each dict for a fist look; list of dicts maybe? {<len>: [{a:1...}...] may have further optimization, but will do.
        anagrams = [] # result
        return_index = {} # index saving were each anagram list is in the final result
        for word in strs:
            # get chars, 
            ## could be cut short for last one with no len match.
            char_count = {}
            for c in word:
                if c in char_count:
                    char_count[c] += 1
                else:
                    char_count[c] = 1
            # check for entries
            key = "".join(sorted(word))
            if key in return_index:
                anagrams[return_index[key]].append(word)
            else: # registers if not already in.
                anagrams.append([word])
                return_index[key] = len(anagrams)-1
        return anagrams

        