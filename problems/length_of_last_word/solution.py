class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        wordStart = False
        wordEnd = False
        word = 0
        for i in s[::-1]:
            if i != " ":
                wordStart = True
                word += 1
            if i == " " and wordStart:
                break
        return word            
