"""
Maximum Product Subarray
Leetcode Medium Problem

Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:
  Input: [2,3,-2,4]
  Output: 6
  Explanation: [2,3] has the largest product 6.

Example 2:
  Input: [-2,0,-1]
  Output: 0
  Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        curr_max    = nums[0]
        curr_min    = nums[0]
        output      = nums[0]

        for num in nums[1:]:
            max_product = max(max(curr_max*num, curr_min*num), num)
            min_product = min(min(curr_max*num, curr_min*num), num)
            curr_max = max_product
            curr_min = min_product
            output = max(output, max_product)


        return output
