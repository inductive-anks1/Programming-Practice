# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:48:52 2022

@author: kumar
"""
import numpy as np
import matplotlib.pyplot as plt
import time

def matrix_product(M, N):
    rows = N.shape[0]
    cols = M.shape[1]
    
    if rows != cols:
        return None
    
    rows = M.shape[0]
    cols = N.shape[1]
    
    A = np.zeros((rows, cols))
    
    for i in range(rows):
        for j in range(cols):
            A[i, j] = sum(M[i, :] * N[:, j])
    
    return A


np_avg = []
my_avg = []

i = 2
while i < 129:
    np_time = []
    my_time = []
    
    M = np.random.rand(i, i)
    
    for j in range(30):
        st = time.time()
        matrix_product(M, M)
        et = time.time()
        my_time.append(et-st)
    my_avg.append(np.average(my_time))
    
    for j in range(30):
        st = time.time()
        np.matmul(M, M)
        et = time.time()
        np_time.append(et-st)
    np_avg.append(np.average(np_time))
    
    i = i * 2
    
X = np.arange(len(np_avg))
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(X + 0.00, my_time, color='orange', width=0.25)
ax.bar(X + 0.25, np_time, color='cyan', width=0.25)
ax.plot(X, my_time, color='orange')
ax.plot(X, np_time, color='cyan')

plt.title("Numpy vectorization v/s Naive algorithm")
plt.xlabel("Dimensions in $2^{x}$")
plt.ylabel("Average Execution Time")
plt.legend()
plt.grid()

plt.show()

            
            