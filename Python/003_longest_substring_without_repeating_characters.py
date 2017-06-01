# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, last = 0, 0, [-1 for _ in xrange(256)]
        for i, char in enumerate(s):
        	if last[ord(char)] >= start:
        		start = last[ord(char)] + 1
        	longest = max(longest, i-start+1)
        	last[ord(char)] = i

        return longest

if __name__ == '__main__':
	print Solution().lengthOfLongestSubstring("abc-c--defg")

