from collections import Counter

# Runtime 58 ms
# Memory  13.9 MB

class Solution:
    def topKFrequent(self, words: list[str], k: int):

        alphabeticalSort = sorted(words)
        
        CounterObj = Counter(alphabeticalSort)
        
        TopkFreq = CounterObj.most_common(k)
        
        TupleZipping = zip(*TopkFreq)
        
        ReturnKeys = next(TupleZipping)
        
        return ReturnKeys

# Learn to use Counter object

# Sample 41 ms submission

class Solution:
    def topKFrequent(self, words: list[str], k: int):
        # Get the frequency of each word
        freq = Counter(words)
        
        # Sort the words by frequency
        # If the frequency is the same, sort by alphabetical order
        sorted_words = sorted(freq, key=lambda x: (-freq[x], x))
        
        # Return the top k words
        return sorted_words[:k]