class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_numsMap = {}
        for number in nums:
            if number in count_numsMap:
                return True
            else:
                count_numsMap[number] = 1
        return False
        
            
