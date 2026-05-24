class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for one in nums:
            if one == 1:
                count += 1
                if count >= max_count:
                    max_count = count
                continue
            else:
                count = 0
                continue
        return max_count