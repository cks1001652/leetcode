class Solution:
    # Not using string conversion

    # build up the reverse number using reminder
	def isPalindrome(self, x: int) -> bool:
		reverse = 0
		number = x
		while (number > 0):
			reminder = number % 10  # getting last digit (units) from the number
			reverse = (reverse * 10) + reminder  # creating new reversed number
			number = number // 10  # getting the number without last digit (cutting units)

		
		if x >= 0 and x == reverse:    # x has to be bigger than 0 because negative numbers don't meet the criteria
			return True
		else:
			return False

# 1221
# r = 1
# re = 1
# n = 122

#r = 2
#re = 10+2 = 12
# n = 12
