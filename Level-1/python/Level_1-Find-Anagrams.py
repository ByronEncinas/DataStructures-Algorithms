# https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples
# https://leetcode.com/problems/find-all-anagrams-in-a-string/solutions/3148122/well-explained-beats-98-96-o-n-time-complexity-o-1-space-complexity/
from collections import Counter

## My solution, sadly too slow

"""             Video Analysis: https://www.youtube.com/watch?v=G8xtZy0fDKg

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # initialize variables
        windowsize = len(p)
        stringsize = len(s)

        # base case
        if windowsize > stringsize: return answer

        phash, shash = dict(), dict()
        # create hashmap of p and first windowsize hashmap of s
        for i in range(windowsize):
            phash[p[i]] = phash.get(p[i],0) + 1
            shash[s[i]] = shash.get(s[i],0) + 1

        # if both are equal
        if phash == shash:
            answer = [0]
        else:
            answer = []

        l = 0 # left pointer 
        for rpointer in range(windowsize,stringsize):
            shash[s[rpointer]] = shash.get(s[rpointer], 0) + 1 ## add next
            shash[s[l]] -= 1 # remove prev

            if shash[s[l]] == 0:
                shash.pop(s[l])
            l += 1
            if shash == phash:
                answer.append(l)
        return answer




"""

class Solution:
    def findAnagrams(self, text: str, word: str):
        # sliding window technique
        # our window's size
        win = len(word)
        # window possible steps.
        rg = len(text) - win + 1
        # output
        indices = []

        for idx in range(rg):
            #print(text[idx:idx+win])
            if isAnagram(text[idx:idx+win], word): 
                indices.append(idx)
            else:
                continue
        return indices

def isAnagram(text1: str, text2: str) -> bool:
    # compares two string and founds if text1 and text2 are
    # each an anagram of the other
    # list of letters to slid into
    s1 = list(text1)
    s2 = list(text2)
    isanag = (Counter(s2) - Counter(s1)).values() 
    if len(isanag) == 0:
        return True
    else:
        return False

## 95 ms

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        windowsize = len(p)
        stringsize = len(s)
        answer = []
        
        # base case, cannot find anagram if windowsize > stringsize
        if windowsize > stringsize: return answer              # --> []

        # size 26 for ocurrence in any of the 26 letters
        wantedletters = [0 for _ in range(26)]
        currentletters = [0 for _ in range(26)]

        # measure ocurrence of any of 26 letters in p
        for letter in p:
            wantedletters[ord(letter)-97] += 1

        # measure ocurrence of any of 26 letters 
        for i in range(windowsize):
            currentletters[ord(s[i])-97] += 1                  # <-- measure ocurrence of letters in s

        if currentletters == wantedletters:                    # <-- if equal add a solution at answer
            answer.append(0)

        # here we look for the index into which those solutions are
        for i in range(windowsize,stringsize):                 # <-- window sliding
            currentletters[ord(s[i-windowsize])-97] -= 1
            currentletters[ord(s[i])-97] += 1
            
            if currentletters == wantedletters:
                answer.append(i+1-windowsize)

        
        return answer