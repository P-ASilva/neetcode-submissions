class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # First Hypothesis: iter once, record counts in dict. CORRECT 
        # Time: O(n), Space: O(n/2)? 
        # Cuz at least half will be recorded in the same entry?
        # EXTRA : could you do it in O(1) Space?
        # well, on a sorted list it would be as simple as counting in intervals depending on the recorded number, them returning when it reachs n/2.
        # Second Hypothesis: sort, iter once, them count equal numbers until it reaches a new number or n/2.
        # Time O(n log(n)), Space O(1), being a tradeoff of time for space.
        # Third Hypothesis: iter making removals, once for every number until one reaches n/2.
        # Time O(n²) Space O(1)
        # Best one is Boyer-Moore Voting Algorithm; which simulates the behaviour of hypothesis three - if the structure was not a list and rather a linked list or node tree the third hypothesis would be the same. Issue is in O(n) removal time for each item
        index = {}
        curr_max = nums[0]
        index[nums[0]] = 1
        for num in nums[1:]:
            # increase count
            if num in index:
                index[num] += 1
            else:
                index[num] = 1
            # replace record
            if index[num] > index[curr_max]:
                curr_max = num
            if index[curr_max] > len(nums)/2:
                break
        return curr_max
        
