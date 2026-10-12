class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # python sort works in O(n log n) and space O(1) / O(n)
        # mostly due to subdividing
        index = set()
        for num in nums:
            if num in index:
                return True
            else:
                index.add(num)
        return False