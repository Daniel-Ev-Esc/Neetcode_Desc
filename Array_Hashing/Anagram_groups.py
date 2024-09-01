# 01/09/2024
# Anagram groups
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        finalList = []

        anagramsDict = {}

        groups = 0
        for s in strs:
            thisAnagram = ''.join(sorted(s))
            if thisAnagram in anagramsDict:
                finalList[anagramsDict[thisAnagram]].append(s)
            else:
                finalList.append([s])
                anagramsDict[thisAnagram] = groups
                groups+=1

        return finalList
    
solution = Solution()

print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

# Neetcode solution
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = defaultdict(list)

#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
    #         Can use tuple as keys
#             ans[tuple(count)].append(s)

    #     Returns the list of list
#         return ans.values() 