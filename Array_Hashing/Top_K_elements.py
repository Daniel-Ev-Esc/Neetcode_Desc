# 01/09/2024
# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicto = {}

        for element in nums:
            dicto[element] = 1 + dicto.get(element, 0)

        sorted_element = sorted(dicto.items(), key=lambda x:x[1], reverse=True)

        finalList = []

        for i in range(k):
            finalList.append(sorted_element[i][0])

        return finalList
    
solution = Solution()

print(solution.topKFrequent([1,2,2,3,3,3],2))
print(solution.topKFrequent([7,7],1))