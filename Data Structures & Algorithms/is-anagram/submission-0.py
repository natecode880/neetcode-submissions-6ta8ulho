class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(list(s)) != len(list(t)):
            return False
        
        count_s = {}
        count_t = {}
  
        for s in s:
            count_s[s] = count_s.get(s, 0) + 1
        
        for t in t:
            count_t[t] = count_t.get(t, 0) + 1

        return count_t == count_s
            
            
        