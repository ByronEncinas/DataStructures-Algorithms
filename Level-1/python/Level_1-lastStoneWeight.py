## Time: 43 ms - Space: 13.9 MB

class Solution:
    def lastStoneWeight(self, stones):
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        
        stn1 = max(stones)          # max of stones = [...,...,...,...] 
        stones.remove(stn1)
        stn2 = max(stones)          # 2nd maximium in stones
        stones.remove(stn2)         # remove 2nd max from stones   
        if stn1 == stn2:
            return self.lastStoneWeight(stones)
        elif stn1 != stn2:
            new_boulder = abs(stn1 - stn2)
            stones.append(new_boulder)
            return self.lastStoneWeight(stones)
        

""" 
NEED FOR STUDY: heap data structure

"""

## Time: 12 ms

from heapq import heappush, heappop, heapreplace
class Solution2:
    def lastStoneWeight(self, stones) -> int:
        hq = [-x for x in stones]
        hq.sort()

        while (ts := heappop(hq)) and hq and (s := hq[0]):
            if ts == s:
                heappop(hq)
                if not hq:
                    return 0
            else:
                heapreplace(hq, ts - s)
        return -ts
            