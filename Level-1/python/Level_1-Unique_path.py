
class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        # Dynamic Programming, this is the gridTraveler
        key = str(m) + ','+ str(n) ## concatena m,n como un key

        if (m == 1 and n == 1):
            memo[key] = 1
            return 1
        if (m == 0 or n == 0):
            memo[key] = 0
            return 0
        if (key in memo):
            return memo[key]
        else:    
            memo[key] = self.uniquePaths(m-1,n, memo) + self.uniquePaths(m,n-1, memo)
            return memo[key]


# Best runtime 8 ms
def util(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if n in util.mem:
        return util.mem[n]
    
    util.mem[n] = util(n-1) + util(n-2)
    return util.mem[n]
    

class Solution:
    def climbStairs(self, n: int) -> int:
        util.mem = {}
        return util(n)

#
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [1]*n for i in range(m)]

        for y in range(1,m):
            for x in range(1,n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

        return dp[m-1][n-1]