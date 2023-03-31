'''
Leetcode Problem - 
https://leetcode.com/problems/binary-search/
'''

#Solution - 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            midElement = (start + end) // 2
            if nums[midElement] == target:
                return midElement
            elif target < nums[midElement]:
                end = midElement - 1
            else:
                start = midElement + 1
        
        return -1
        
