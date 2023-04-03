'''
Problem - https://leetcode.com/problems/reverse-string/
'''

# Solution - 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper (left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
        helper(0, len(s) - 1)
        
