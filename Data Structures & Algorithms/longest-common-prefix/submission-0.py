class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # max pref size is min str size.
        # fastest way is to iter simultaneously betwen all strs, as O will be 
        ## O(i * n) with i being the prefix size + 1 and n the amount of strs, with i ~ 1 in big O, also with space O(i) or O(1) by the same logic.
        # can be faster/smarter?
        ## well. We can do "two pointer" comparisons, since the prefix must be global.
        ### the result will still be O(n), since we must ensure i applies to all strs, but we need not worry about index overflows. This 'saves' on a few if statements. We can also skip the first iteration, by stating the first hypothetical prefix is the full first string, them, we save on a few more iters on the for by checking the last char in the hypothesis first, and decend from there. Could be brought further, by employing a pseudo binary search, but that seems like too much work and reaching a little.
        # I will do the pointer approach, with no chars search optimizations.
        def iter_common_prefix(prefix: str, str2: str) -> str: 
            cprefix = ""
            for i in range(len(prefix)):
                if i >= len(str2) or prefix[i] != str2[i]:
                    break
                elif prefix[i] == str2[i]:
                    cprefix += prefix[i]
            return cprefix

        prefix = strs[0]
        for word in strs[1:]:
            prefix = iter_common_prefix(prefix, word)
            if prefix == "": break
        


        return prefix
                

