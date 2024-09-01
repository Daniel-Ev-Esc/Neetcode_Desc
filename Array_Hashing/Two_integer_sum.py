# 01/09/2024
# Two integer sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i in range(0, len(nums)):
            if target - nums[i] in dict:
                return [dict[target-nums[i]], i]

            if nums[i] not in dict:
                dict[nums[i]] = i


solution = Solution()

print(solution.twoSum([3,4,5,6], 7))
print(solution.twoSum([4,5,6], 10))
print(solution.twoSum([5,5], 10))
