def fibo_recursive(n):
    
    if n == 0:
        return 0
    elif (n == 1):
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
    
##print(fibo_recursive(5))
