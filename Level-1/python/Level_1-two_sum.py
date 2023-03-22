class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash = dict()

        for index, value in enumerate(nums):
            complement = target - value
            if complement in hash:
                return [index, hash[complement]]
            else:
                hash[value] = index

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash = dict()
        iter = 0
        while target - nums[iter] not in hash:
            hash[nums[iter]] = iter
            iter += 1
        
        return iter, hash[target - nums[iter]]
            
