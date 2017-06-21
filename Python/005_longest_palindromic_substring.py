#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example:

#Input: "babad"

#Output: "bab"

#Note: "aba" is also a valid answer.
#Example:

#Input: "cbbd"

#Output: "bb"

class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype str
		""" 
		start, end = 0, 0
		for i in xrange(0,len(s)):
			len_odd = self.expandCenter(s, i, i)
			len_even = self.expandCenter(s, i, i+1)
			len_max = max(len_even, len_odd)

			if len_max > (end - start + 1):
				start = i - (len_max - 1) / 2
				end = i + len_max/2

		return s[start:end+1]
			

	def expandCenter(self, s, left, right):
		L, R = left, right
		while (L >= 0) and (R < len(s)) and (s[L] == s[R]):
			L-=1
			R+=1
		return R - L - 1

if __name__ == '__main__':
	result = Solution().longestPalindrome("abbcde")
	print(result)
