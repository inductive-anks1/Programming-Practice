import matplotlib.pyplot as plt
import math
import numpy as np

def cycloid(r):  # Function defination for Cycloid plot
    x = []       # List of x coordinates
    y = []       # List of y coordinates
    
    for theta in np.linspace(0, 4*np.pi, 100):
        x.append(r*(theta - np.sin(theta)))
        y.append(r*(1- np.cos(theta)))
        plt.plot(x,y)
        #plt.gca().set_aspect('equal')
        plt.axis('square')
        plt.show()
        
cycloid(100)

        
