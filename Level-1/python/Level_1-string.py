""" 
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

  """


""" 
This is the most efficient in LeetCode
"""
class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s))!=len(set(t)):
            return False
        else:

            dict={}
            for i in range(len(s)):
                dict[s[i]]=t[i]
            flag=True
            for i in range(len(s)):
                if dict[s[i]]!=t[i]:
                    return False
                    flag=False
            return flag

""" 
This was my implementation for the problem
"""
class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## if both string are different size then close
        if len(s) != len(t):
            return False
        for index, letter in enumerate(s):
            key = t[index]
            if s.index(letter) != t.index(key):
                return False
        return True
    

class Solution5(object):
    def isIsomorphic(self, s, t):
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))


"""  
Given two strings s and t, return true if s is a subsequence of t, 
or false otherwise. A subsequence of a string is a new string that 
is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the 
remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" 
is not).
"""
## Best solution in time

class Solution3(object):
    def isSubsequence(self, s, t):
        if len(t) < len(s):
            return False

        last_index = 0
        for i in range(0, len(t)):
            if last_index <= len(s) - 1 and s[last_index] == t[i]:
                last_index += 1

        return last_index == len(s)

## My solution
class Solution4(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) >= len(t):
            return False
        count = 0
        while len(s) != 0:
            ## current letter s[0]
            index = t.find(s[0])
            if index == -1:
                return False

            t = t[index+1:]
            s = s[1:]
            count += 1

        return True