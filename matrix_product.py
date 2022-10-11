import numpy as np
import time
import matplotlib.pyplot as plt

def matrix_product(A,B):
    
    p = len(A)
    q = len(A[0])
    
    t = len(B)
    r = len(B[0])
    
    if (q != t):
        quit()  
    
    C = []
    
    for row in range(p):
        curr_row = []
        for col in range(r):
            curr_row.append(0)
        C.append(curr_row)
    
    
    for i in range(p):
        for j in range(r):
            curr_val = 0
            for k in range(q):
                curr_val += A[i][k] * B[k][j]
            C[i][j] = curr_val
            
    return C

def matrix_product_naive():
    my_time = []
    np_time = []
    length = []
    i = 2
    while i < 1025:
        A = np.random.rand(i, i)
        B = np.random.rand(i, i)  
    
        st = time.time()
        C = matrix_product(A, B)
        et = time.time()
        my_time.append(et - st)
        
        st = time.time()
        C = (np.matmul(A,B))
        et = time.time()
        
        np_time.append(et-st)
        
        length.append(i)
        i *= 2
        
    plt.plot(length, my_time)
    plt.plot(length, np_time)
    plt.show()
    
matrix_product_naive()

        
    




    

        