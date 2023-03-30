//run using node tabul.js

// Tabulation
// time: O(n) 

const fib = (n) => {
    const table = Array(n+1).fill(0);
    table[1] = 1;
    for (let i = 0; i <= n; i++) { 
        table[i+1] += table[i];
        table[i+2] += table[i];
    };
    return table[n]
};

console.log(fib(50)) 

//run using node tabul.js

// Tabulation
// time & space: O(m*n) 
 
const gridTraveler = (m, n) => {
    // create matrix m+1 x n+1
    const table = Array(m + 1)
        .fill(0)
        .map( () => Array(n + 1).fill(0) );

    table[1][1] = 1;

    console.log(table)
    for (let i = 0; i <= m; i++){
        for (let j = 0; i <= n; i++){
            const current = table[i][j];
            if (j + 1 <= n) table[i][j + 1] += current;
            if (i + 1 <= m) table[i + 1][j] += current;
        }
    }
    return table[m][n]
};

console.log(gridTraveler(1, 1))

//run using node tabul.js

// Tabulation
// time & space: O() 