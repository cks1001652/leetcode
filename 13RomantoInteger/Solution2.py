class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        # initialize the result and position to 0 and 'I'
        res, p = 0, 'I'
        # for each item in the reversed string
        for item in s[::-1]:
            # if the value of the current item from the reversed string < value of previous item, substract the value of current item 
            # otherwise add the value of current item
            # i.e for string IX, reversed = XI, since I:1 <X:10 then res = 10 - 1 = 9 
            res, p = res - d[item] if d[item] < d[p] else res + d[item], item
        return res    