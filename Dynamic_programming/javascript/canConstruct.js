/* Main change here is that we are looking to adhere to
words that may be found in the beginning of the 
target */

/* Such that if target = 'abcdef' and in the ith iteration
we have word = 'abc' then target.indexOf(word) = 0
because we have it at the beginning of the target, therefore
we can cut it of and continue to branch */

/* > target = 'patata'
'patata'
> target.indexOf('pat')
0
> target.slice('pat'.length)
'ata' 
> */

const canConstruct_ = (target,wordbank) => {
    if (target === '') {
        return true;
    }
    for (let word in wordbank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            
            
            if (canConstruct_(suffix, wordbank) === true) {
                return true
            }

        }
    }
    return false
};

/* Let's analyze and memoize */

/* Let's check tree length */

/* 
target_ = 'enterapotentpot'
wordbank_ = [a,p,ent,enter,ot,o,t]
 */

/* 
m = target.length
n = wordbank.length

The height of the tree will be in the worst case m
such that the tree will be branched at worst n times per level.
and then, we will take the slicing method add a m multipied
then we will have a time complexity 

time: O(n^m*m)
space: O(m^2)

*/

const canConstruct = (target, wordbank, memo = {}) => {
    if (target in memo) return memo[target];
    if (target === '') return true;
    
    for (let word in wordbank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            
            if (canConstruct(suffix, wordbank,memo) === true) {
                memo[target] = true
                return true
            }

        }
    }
    memo[target] = false
    return false
};

/* 

m = target.length
n = wordbank.length

time: O(n*m^2)
space: O(m^2)

*/