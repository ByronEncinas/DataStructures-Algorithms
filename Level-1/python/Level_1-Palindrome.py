## Mine
class Solution1:
    def longestPalindrome(self, s: str) -> int:
        ## if string is already a palindrome        
        hasht = dict()
        palin_length = 0
        for lyr in s:
                ## we will count occurrence of each letter
                hasht[lyr] = hasht.get(lyr, 0) + 1
                if hasht[lyr] % 2 == 0:
                    #it means we got another even occurrence of elems in string
                    palin_length += 2
                if palin_length == len(s):
                    # if size of s is same as palindrome, there is no need for +1
                    # at the end, so we take it out
                    palin_length -= 1


        return palin_length +1

## best time
from collections import Counter
class Solution2:
    def longestPalindrome(self, s: str) -> int:
        mem = Counter(s)
        t = 0
        f = False
        for char in mem:
            if mem[char] % 2 == 1:
                if not f:
                    t += mem[char]
                    f = True
                else:
                    t += mem[char] - 1
            else:
                t += mem[char]
        return t

