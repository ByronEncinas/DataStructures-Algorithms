// We are gonna be working 
// in javascript to learn
// how to problem solve 
// using code

// We will be implementing the base cases in a const function with in variables m,n

const gridTraveler_ = (m,n) => {
    if (m === 1 && n === 1) return 1;
    if (m === 0 || n === 0) return 0;
    return gridTraveler_(m-1,n) + gridTraveler_(m,n-1);
};

console.log(gridTraveler_(3,3))

// but if (m,n) = (18,18) it gets slow


// Let's try add memoization before continuing with the video

const gridTraveler = (m,n, memo = {}) => {
    // are the args in memo
    // we add new contstant
    const key = m + ',' + n // this aint adding numbers, is concatenation
    if (key in memo) return memo[key]; 
    // if m + n is in the dict called memo
    // then we will save memo[key = m + n] = ##steps used to get there
    if (m === 1 && n === 1) return 1;
    if (m === 0 || n === 0) return 0;
    memo[key] = gridTraveler(m-1,n, memo) + gridTraveler(m,n-1,memo)
    return memo[key];
};


console.log(gridTraveler(4,4))
console.log(gridTraveler(18,18))

// Difference between this ant fibonacci, was only the way we get the memo called up

// In fibonacci we are supposed to take the n-th position and store in memo[n] = fib(n)

// In grid traveler we have not 1, but two positions in both x and y for the grid.
// (m,n) define our entry, but we have discovered that mxn and nxm match exactly in number of ways
// to get from starting position to final position, so we can get a new constant  key = m + n such that
// when we have already calculated the (m,n) or (n,m) anzats we can store it with a identifier m + n
// so memo[ m + n ] = ## number of steps for such grid.

// finally, we already have worked out to implement memoization in both codes successfully.

// Memoized algorithm has a time complexity of O(m * n) 