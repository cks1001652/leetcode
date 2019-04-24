# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        ## if everything match and has the same length, it will be the longest string 
        ## if you mathc a whole string from the list, then it must bbe the string wtith smallest length
        ## otherwise it will be part of the smallest string or nothing
        smin = min(strs)
        smax = max(strs)
        # for each letter of the smallest string
        for n, i in enumerate(smin):
            # if nth letter = the nth letter of max string, then pass and move on to n+1 th lettet
            # if nth letter != nth letter of max string, then we only need all the letter up to n-1th letter of small string
            if i != smax[n]:
                return smin[:n]
        # if all the string match, we pass all condition from the previous loop
        # then return the small string
        return smin

                
