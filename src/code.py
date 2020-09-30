import numpy as np
from scipy import linalg


def sum_numbers(x, y):
    return x+y

def multiply_numbers(x, y):
    return x*y

def create_add_matrix(x):  
    array=np.ones((3,3))
    suma=array+x

    return suma
    
def indexing_aggregation(x, n):
    mean=np.mean(x[:n])
    
    return mean
  
def matrix_inverse(A):
    
    if A.shape[0]!=A.shape[1]:
        print("dimension mismatch")
        return 0
    else:
        inverse=np.linalg.inv(A) 
    
    return inverse

