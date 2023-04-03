'''
Problem - https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''

# Solution - 
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        finalwords = []
        
        for word in words:
            finalwords.append(word[::-1])
        
        return ' '.join(finalwords)
