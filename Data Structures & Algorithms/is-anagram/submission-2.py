class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True

        if len(s) != len(t):
            return False

        string1_chars = sorted(list(s)) #sorts in ascending order
        string2_chars = sorted(list(t)) #sorts in ascending order
        #now an anagram is where the strings contain the same characters, for the same number of times regardless of the order. However, for easy condition and prevention of looping we sort using the built in function sorted to then check if they are exactly equal


        if string2_chars == string1_chars:
            return True
        else:
            return False
