# 01/09/2024
# Duplicate integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        dict = {}

        # I used dict because i was more familiar with it, this should be a set
        for element in nums:
            # If the element was previously added, there is a duplicate
            if element in dict:
                return True
        
            dict[element] = True

        return False
    
solution = Solution()

print(solution.hasDuplicate([1,2,3,3]))
print(solution.hasDuplicate([1,2,3,4]))