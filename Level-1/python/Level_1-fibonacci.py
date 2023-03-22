
from functools import cache

## My recursive Solution 800+ ms

class Solution:
    # @cache is automatic memoization
    @cache    
    # memoization for the last 5 calls
    # @lru_cache(maxsize= 5)
    def fib(self, n: int) -> int:
        if (n <= 1):
            
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

# Another very useful related decorator is "cached_property", which lets you compute a property just once when needed, and remember it as long as the object exists.
# @fib.cache_clear()

## The best Runtime 19 ms
class Solution: 
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev1 = 0
        prev2 = 1
        for i in range(2,n+1):
            ans = prev1 + prev2
            prev1 = prev2
            prev2 = ans
        return ans

class Solution:
    def fib(self, n: int) -> int:
        l = [0,1]
        for i in range(2,n+1):
            l.append(l[i-1]+l[i-2])
        return(l[n])
