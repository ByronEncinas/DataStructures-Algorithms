""" 1480. Running Sum of 1d Array
Easy
6K
289
Companies
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums. """

class Solution1(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums) == 0 or len(nums) == 1: 
            ## if [] or [a] then result is itself
            return nums
        
        ## each time we sum the nums[index] + nums[index-1]
        for index, elem in enumerate(nums):
            if index == 0:
                sum_current = nums[index]
                result.append(sum_current) ## inner base case
            else:
                sum_current = result[index - 1] + nums[index]
                result.append(sum_current) 
        return result
            

""" 
for index = 0
we will sum: nums[0]
for index = 1
we will sum: nums[0] + nums[1]
for index = 2
we will sum: nums[0] + nums[1] + nums[2]
"""

""" 
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution2(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## if we'd rather know the sum of all numbers and not
        ## use sum() repeatedly
        OverallSum = sum(nums)
        leftSum = 0 ## we will be adding to this as for loop progresses
        for index, ith_number in enumerate(nums):
            # we will know if left = OverallSum - leftSum - ith_number = rightSum
            if leftSum == OverallSum - leftSum - ith_number:
                return index
            ## if it (leftSum == OverallSum - leftSum - ith_number) = False
            ## then let's move to leftSum = leftSum + ith_number
            leftSum = leftSum + ith_number
        return -1