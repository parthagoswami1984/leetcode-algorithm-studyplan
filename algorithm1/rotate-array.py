'''
Problem - https://leetcode.com/problems/rotate-array/
'''

# Solution - 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        extra_array = [0] * len(nums)
        for i in range(len(nums)):
            extra_array[(i + k) % len(nums)] = nums[i]
        
        nums[:] = extra_array
        
