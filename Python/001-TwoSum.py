# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer_dic = {}
        for i,num in enumerate(nums):
            if target - num in buffer_dic:
                return [buffer_dic[target - num], i]
            buffer_dic[num] = i
        return []

    def two_sum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            j = target - num
            if j in nums[i+1:]:
                return [i, nums.i(j)]
        return []

if __name__ == '__main__':
    result = Solution().two_sum((1,3,9,7),8)
    print(result)