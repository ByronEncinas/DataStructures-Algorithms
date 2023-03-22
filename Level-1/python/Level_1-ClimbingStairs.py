## My recurisive best time 26ms beats 91%
def steps_calc(n):
    if n in steps_calc.memo:
        return steps_calc.memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    steps_calc.memo[n] = steps_calc(n-1) + steps_calc(n-2)
    return steps_calc.memo[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        """     
        if n <= 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2) 
        """
        steps_calc.memo = {}
        return steps_calc(n) 



## The best Runtime 8 ms
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