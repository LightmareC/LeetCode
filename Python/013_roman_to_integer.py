#Given a roman numeral, convert it to an integer.

#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_dic = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        length = len(s)
        result = 0

        for i, char in enumerate(s):
        	val = value_dic[s[i]]
        	if (i == length-1) or (value_dic[s[i]] >= value_dic[s[i+1]]):
        		result += val
        	else:
        		result -= val

        return result
