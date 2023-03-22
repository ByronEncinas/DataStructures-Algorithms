""" 
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    """ 
    
    ...
    ...
    
    """
    pass

class Solution1:
    def firstBadVersion(self, n: int) -> int:
        return self.search(n)

    def search(self, n: int) -> int:
        left = 1
        right = n  
 
        while left <= right: 
            mid = left + (right - left)//2 
            if isBadVersion(mid) == False: 

                left = mid + 1
            else:
                right = mid - 1
        return left

class Solution2:
    def firstBadVersion(self, n: int) -> int:
        lowerbound = 0
        while n > 0:
            while not isBadVersion(n + lowerbound): 
                lowerbound += n ## lowerbound = lowerbound + n
            n //= 2 ## n = n//2
        return lowerbound + 1


class Solution3:
    def firstBadVersion(self, n: int) -> int:
        # base case
        if n==1 and isBadVersion(n):
            return 1
        # left and right indexes: n indexes in total.
        L, R = 1, n
        # pivot = mid 
        while L < R:
            midpoint = L + (R - L) // 2
            if isBadVersion(midpoint):
                R = midpoint
            elif not isBadVersion(midpoint):
                L = midpoint + 1
        return L