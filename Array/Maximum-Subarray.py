"""
Maximum Subarray
LeetCode Easy Problem

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
  Input: [-2,1,-3,4,-1,2,1,-5,4],
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.
  
Follow up:
  If you have figured out the O(n) solution, try coding another solution using the divide 
  and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:
            curr_max = max(curr_max + num, num)
            max_so_far = max(max_so_far, curr_max)

        return max_so_far
