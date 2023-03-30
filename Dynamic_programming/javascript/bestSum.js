/* bestSum takes (targetSum, numbers) */
/* returns array containing shortest combination that add up
to exactly the targetSum */
/* If there is a tie, it return any */

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
};

/* Now we can work out the memoization */

const bestSum = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum]; /* New line */
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    let shortestCombination = null

    for (let num of numbers) {

        const remainder = targetSum - num;
        const remainderCombination = bestSum(remainder,numbers, memo);
        
        if (bestSum(remainder, numbers, memo) !== null) {
            const combination = [...remainderCombination, num];
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination;
                }
        }
    }
    memo[targetSum] = shortestCombination /* New line */
    return shortestCombination
};


console.log(bestSum(8,[1,3,5]))
console.log(bestSum(8,[1,3,5]))
console.log(bestSum(100,[1,2,5,25]))