from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        
        # One pass to increment and decrement
        for i, j in zip(s, t):
            count[i] += 1
            count[j] -= 1
            
        # Check if all values are 0
        for val in count.values():
            if val != 0:
                return False
                
        return True