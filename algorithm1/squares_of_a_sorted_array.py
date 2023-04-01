'''
Problem - https://leetcode.com/problems/squares-of-a-sorted-array/
'''

# Solution - 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None for _ in nums]        
        start, end, current = 0, len(nums) - 1, len(nums) - 1
        
        while start <= end:
            if nums[start] * nums[start] < nums[end] * nums[end]:
                result[current] = nums[end] * nums[end]
                end -= 1
            else:
                result[current] = nums[start] * nums[start]
                start += 1
            
            current -= 1
        return result
        
            
            
        
