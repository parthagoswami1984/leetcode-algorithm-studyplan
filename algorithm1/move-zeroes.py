'''
Problem - https://leetcode.com/problems/move-zeroes/?envType=study-plan&id=algorithm-i
'''

# Solution - 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_of_zero = nums.count(0)
        for i in range(count_of_zero):
            nums.remove(0)
            nums.append(0)
        
