# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        H = n
        L = 1

        while L <= H:
            mid = (L + H) // 2
            if guess(mid) == 1:
                L = mid + 1
            elif guess(mid) == -1:
                H = mid - 1
            elif guess(mid) == 0:
                return mid               

    def guess(num: int) -> int:
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0
    
        