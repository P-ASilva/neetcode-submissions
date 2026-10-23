class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        # remove val and add it to end
        i = 0
        while i in range(len(nums)):
            if nums[i] == val:
                if (len(nums)-1) >= i + count:
                    count += 1
                    nums.pop(i)
                    nums.append(val)
                    continue
            i+=1
        return len(nums)-count
