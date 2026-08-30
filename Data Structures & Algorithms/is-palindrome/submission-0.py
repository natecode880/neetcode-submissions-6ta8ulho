class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = []

        for char in s:
            if char.isalnum():
                str1.append(char.lower())
    
        l,r = 0, len(str1) - 1
        while l < r:
            if str1[l] != str1[r]:
                return False
            l+=1
            r-=1
                    
        return True
