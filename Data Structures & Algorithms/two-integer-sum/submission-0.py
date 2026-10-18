class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # N log N (sort)
        # N² (iter X iter)

        # pick 1, subtract = number 2, {V:i}
        # if pich 2 == V = return i, i_pick_2

        complement = {}
        for i in range(len(nums)):
            temp_target = target - nums[i] # success condition for number i pair
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[temp_target] = i
