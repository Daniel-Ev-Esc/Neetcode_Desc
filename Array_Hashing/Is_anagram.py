# 01/09/2024
# Is anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        # This function can be simplified by using the get method of dict, in which the alternative value of 0 can be specified
        def addToDict(char: str, dict:dict):
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 0

        if len(s) != len(t):
            return False
        
        dict1 = {}
        dict2 = {}
        
        for i in range(0, len(s)):
            addToDict(s[i], dict1)
            addToDict(t[i], dict2)

        return dict1 == dict2

solution = Solution()

print(solution.isAnagram("racecar", "carrace"))
print(solution.isAnagram("jar", "jam"))