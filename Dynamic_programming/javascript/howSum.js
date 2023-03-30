

const howSum = (target, numbers, memo = {}) => {
    if (target in memo) return memo[target];
    if (target === 0) return [];
    if (target < 0) return null;

    for (let num of numbers) { /* Careful using "in" instead of "of" */
        const remainder = target - num;
        const result = howSum(remainder, numbers, memo);
        if (result !== null) {
            memo[target] = [ ...result, num]
            return memo[target];
        }
    }
    memo[target] = null;
    return null;
};

/* We will use a spread operator [...arr, 'a', 'b'] that appends one array to a new one*/

console.log(howSum(7,[2,3]))
console.log(howSum(7,[2,4]))
console.log(howSum(8,[2,3,5]))
console.log(howSum(300,[7,14])) 

/* Time complexity is based on the same complexity tree of canSum  */

// Brute force
// time: O(n^m + m)
// space: O(m)

// Memo
// time: O(n*m *m) 
// space: O(m *m) space ocupies a maximum of m arrays of m length
