""" Too much damn many ways to tackle this in python """


""" list modification takes much time and resources
.copy of new_list = list[:] are ways of not appending
we can also concatenate

 """

def bestSum(targetSum,numbers, memo={}):
    
    if targetSum in memo: return memo[targetSum]
    if targetSum==0: return []
    if targetSum<0: return None

    shortestComb = None
    
    for num in numbers:

        remainder = targetSum-num
        remainderCombination = bestSum(remainder,numbers,memo)
        
        if remainderCombination != None:

            remainderCombination = remainderCombination.copy() + [num]
            
            if shortestComb ==  None or len(shortestComb) > len(remainderCombination):
                
                shortestComb=remainderCombination
    
    memo[targetSum]=shortestComb           
    
    return shortestComb



if __name__ == '__main__':

    print(bestSum(4,[2,1,5]))

    print(bestSum(100,[1,2,5,25]))

""" 
    const bestSum_ = (targetSum, numbers) => {
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    let shortestCombination = null
    
    for (let num of numbers) {
        const remainder = targetSum - num;
        const remainderCombination = bestSum_(remainder,numbers);
        
        if (bestSum_(remainder, numbers) !== null) {
            const combination = [...remainderCombination, num];
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination;
            }
        }
    }
    return shortestCombination
}; """