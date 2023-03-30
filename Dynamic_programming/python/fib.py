## We are gonna be working 
## in javascript to learn
## how to problem solve 
## using code

## We'll be writing a function fib(n) that takes in a number as an argument.
## The function should return the n-th number of the fubonacci seq.

## The 1st and 2nd number of the sequence is 1.

## To generate the next number, we sum the previous two.

## n:        1   2   3   4   5   6   7   8   9   10  11
## fib(n):   1   1   2   3   5   8   13  21  ...

## We will take a recursive implementation

from functools import cache

@cache
def fib_(n):
    
    if (n <= 2):
        return 1
    else:
        return fib_(n - 1) + fib_(n - 2)


##print(fib(50))

## the latter piece of code checks for the first cases for n = 1,2 and
## the, starts adding terms once we have tow previous values to add up

#console.log(fib_(6))
#console.log(fib_(7))
#console.log(fib_(8))
##console.log(fib_(50)) ##will crash

## console.log(fib(50)) if we evaluate n = 50 the terminal gets stuck

## why? Take a look at the algorithmic tree
##/ We want to store or capture results

## Memoization: 

##/ We will create and object

#const fib = (n, memo = {} ) => {
#    if (n in memo) return memo[n];
#    if (n <= 2) return 1;
#   memo[n] = fib(n - 1, memo) + fib(n - 2,memo);
#   return memo[n];
#};

memo = {1:1, 2:1}

def fib(n):

    if (n in memo):
        return memo[n]
    else:
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(50))

##/run using python fib.py

