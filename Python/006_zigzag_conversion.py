#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number of rows:

#string convert(string text, int nRows);
#convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: str
		:rtype: str
		"""
		len_src = len(s)
		result = ""

		if len_src == 0 or numRows < 2:
			return s

		for i in range(0, numRows):
			for j in range(i, len_src, 2*numRows-2):
				result += s[j]
				if i > 0 and i < numRows-1:
					index = j + 2*numRows - 2 - 2*i	
					if index < len_src:
						result += s[index]

		return result

if __name__ == '__main__':
	print Solution().convert("PAYPALISHIRING", 3)


