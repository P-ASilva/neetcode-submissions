class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # first hypothesis: iter once, record counts in dict. CORRECT 
        # Time: O(n), Space: O(n/2)? cuz at least half will be recorded in the same entry?
        # EXTRA : do it in O(1)
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
        return curr_max
        
