def fibo_iterative(n):
    
    prevNum = 0
    currentNum = 1
    
    for i in range(2, n):
        prevPrevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prevPrevNum
    return currentNum

print(fibo_iterative(6))