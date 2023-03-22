class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        
        while right >= left: 
            mid = (right + left)//2
            if nums[mid] < target : # [0,2,4,6,8,10] -> 9 > 6
                left = mid + 1    # right = 3 - 1
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                return mid
        return -1
    
