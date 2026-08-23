class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibilities = {} # e.g. {3: 0, 4: 1}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in possibilities:
                return [possibilities[complement], i]
            possibilities[nums[i]] = i
        return []