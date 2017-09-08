#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321

#click to show spoilers.

#Note:
#The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x < 0:
			return -self.reverse(-x)
		result = 0
		while x:
			result = result * 10 + x % 10
			x/=10
		return result if result < 0x7FFFFFFF else 0

if __name__ == '__main__':
	print(Solution().reverse(-123))