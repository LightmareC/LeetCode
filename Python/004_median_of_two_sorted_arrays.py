#There are two sorted arrays nums1 and nums2 of size m and n respectively.

#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#Example 1:
#nums1 = [1, 3]
#nums2 = [2]

#The median is 2.0

#Example 2:
#nums1 = [1, 2]
#nums2 = [3, 4]

#The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total & 0x1:
        	return self.findKth(nums1, nums2, total/2 + 1)
        else:
        	return (self.findKth(nums1, nums2, total/2 ) + self.findKth(nums1, nums2, total/2 + 1)) / 2.0

    def findKth(self, nums1, nums2, k):
     	m, n = len(nums1), len(nums2)
     	if m > n: 
     		return self.findKth(nums2, nums1, k) 
     	if m == 0:
     		return nums2[k-1]
     	if k == 1:
     		return min(nums1[0], nums2[0])

     	i1 = min(m, k/2)
     	i2 = k - i1

     	if nums1[i1-1] < nums2[i2-1]:
     		return self.findKth(nums1[i1:], nums2, k - i1)
     	elif nums1[i1-1] > nums2[i2-1]:
     		return self.findKth(nums1, nums2[i2:], k - i2)
     	else:
     		return nums1[i1-1]

if __name__ == '__main__':
	nums1 = [1, 2]
	nums2 = [3, 4]
	print(Solution().findMedianSortedArrays(nums1,nums2))
     	