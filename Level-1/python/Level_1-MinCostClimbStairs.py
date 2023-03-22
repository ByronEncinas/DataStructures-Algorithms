# Mine but Time Limit Exceded
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """  
        cost = [10,15,20]
        We will branch between 2 firsts steps.
        branch:
            > from index = 0 and on
            > from index = 1 and on
        """
        cost.append(0)
        n = len(cost) - 1
        return self.minCost(cost, n)


    def minCost(self, cost, n):
                
        if n <= 0:
            return cost[0]
        if n == 1:
            return cost[1]
        return min(self.minCost(cost, n-1) + cost[n], self.minCost(cost, n-2) + cost[n])

# Other

class Solution1:
    def minCostClimbingStairs(self, cost) -> int:
        """  
        cost = [10,15,20]
        We will branch between 2 firsts steps.
        branch:
            > from index = 0 and on
            > from index = 1 and on
        """
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])