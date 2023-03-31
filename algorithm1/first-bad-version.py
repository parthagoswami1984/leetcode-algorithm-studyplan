'''
Problem - 
https://leetcode.com/problems/first-bad-version/
'''

# Solution - 
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while start < end:
            midVersion = start + (end - start) // 2
            
            if isBadVersion(midVersion):
                end = midVersion
            else:
                start = midVersion + 1
        
        return start
