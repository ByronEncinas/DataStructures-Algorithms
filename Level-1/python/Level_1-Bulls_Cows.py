from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretList = list(secret)
        guessList = list(guess)
        
        bullCount = 0

        for idx in range(len(guessList)):
            if secretList[idx] == guessList[idx]:
                bullCount += 1

        cowsCount = len(secretList) - bullCount - sum((Counter(secretList) - Counter(guessList)).values()) 

        return ''.join(str(bullCount) + 'A' + str(cowsCount) + 'B')



a = Solution()
b = a.getHint('1346', '1648')
print(b)