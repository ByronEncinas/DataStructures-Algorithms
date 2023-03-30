
## Basicly we want a True or False that answers the question:

## ¿It is possible to add array = [...] elements to targetSum?


def canSum_(targetSum, numbers):
    if (targetSum == 0):
        return True
    if (targetSum < 0): 
        return False ## base cases
## we will try consecutive addings up to finding one
    print(targetSum)
    for x in numbers:
        remainder = targetSum - x
        if (canSum_(remainder,numbers) == True):
            return True
        
    return False



## Now let memoize


def canSum(targetSum, numbers, memo = {}):
    
    keytuple = (targetSum, tuple(numbers))
    
    if (keytuple in memo):
        return memo[keytuple]
        
    if (targetSum == 0):
        memo[targetSum] = True
        return True
    if (targetSum < 0): 
        memo[targetSum] = False
        return False ## base cases

## we will try consecutive addings up to finding one

    for num in numbers:
        remainder = targetSum - num
        
        if (canSum(remainder,numbers, memo) == True):
            memo[keytuple] = True
            
            return True
    
    memo[keytuple] = False    
    return False

## Now let memoize, This implementation does not belong to me, but somehow

print(canSum(7,[2,2])) #--> Es False

print(canSum(7,[2,1])) #--> Es True pero responde False

print(canSum(300,[7,14]))# --> Es False


#url = "https://stackoverflow.com/questions/65428535/why-does-this-solution-work-in-javascript-but-not-in-python-dynamic-programmin"

## Este link contiene información sobre el funcionamiento de python
## y por qué es que una báasica implementación de la memoización no 
## parece funcionar igual que en JS



