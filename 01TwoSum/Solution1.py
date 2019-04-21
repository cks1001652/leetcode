class Solution:
    # Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    ##### Example #####
    # Given nums = [2, 7, 11, 15], target = 9,

    # Because nums[0] + nums[1] = 2 + 7 = 9,
    # return [0, 1].
    
    # idea is to save the residual (target - number) as index and save the index as values
    # then check if the next number = residual (whether it is in the keys) 
    # then return the current index and the value of residual (index of target - value)

    # analysis: there are only one pair of answer for the target, hence we can use residual as dictionary key
    def twoSum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums): 
            if n in dic:
                # if value n is in the dictionary
                return [dic[n], i]
                # return [dictionary values of (value = n), index of value n]
            dic[target-n] = i
            # dictionary[target - value n] = index of value n
