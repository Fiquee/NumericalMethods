import numpy as np
import os


def make_diagonal_dominant(matrix, b):
    max_col_index = np.argmax(np.abs(matrix), axis=0)
    matrix = matrix[max_col_index]
    b = b[max_col_index]

    return matrix, b

def jacobi(matrix,iteration,b, x=None):
    
    if x is None:
        x = np.zeros(len(matrix[0]))
    
    D = np.diag(matrix)
    R = matrix - np.diagflat(D)
    # test = np.diagflat(D)
    
    # print(D)
    # print()
    # print(R)

    for i in range(iteration):
        x = (b - np.dot(R,x)) / D
        print(f'Iteration {i+1}:\n x = {x}')
    return x

    



A = np.array([[5,1,2],[1,4,1],[2,2,5]])
b = np.array([1,2,3])



# A, b = make_diagonal_dominant(A,b)
print(A)
# print(A)
# print("\n",b)

jacobi(A,3,b,[1,1,1])





