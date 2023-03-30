def gridTraveler_(m,n):
    if (m == 1 and n ==1):
        return 1
    if (m == 0 or n == 0):
        return 0
    else:
        return gridTraveler_(m-1,n) + gridTraveler_(m,n-1)

## Lets implement memoization
memo = {}

def gridTraveler(m,n):
    key = str(m) + ','+ str(n) ## concatena m,n como un valor index
    if (key in memo):
        return memo[key]

    if (m == 1 and n == 1):
        memo[key] = 1
        return 1
    if (m == 0 or n == 0):
        memo[key] = 0
        return 0
    if (key in memo):
        return memo[key]
    else:    
        memo[key] = gridTraveler(m-1,n) + gridTraveler(m,n-1)
        return memo[key]


        
print(gridTraveler(3,3))
print(gridTraveler(4,4))
print(gridTraveler(18,18))
