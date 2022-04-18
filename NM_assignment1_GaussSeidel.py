import numpy as np


def make_diagonal_dominant(matrix, b):
    max_col_index = np.argmax(matrix, axis=0)
    matrix = matrix[max_col_index]
    b = b[max_col_index]

    return matrix, b

def GaussSeidel(matrix,b,iteration,x=None):

    if x is None:
        x = np.zeros(len(matrix[0]))

    for iterations in range(iteration):
        for i in range(len(matrix[0])):
            d = b[i]

            for j in range(len(matrix[0])):
                if( i != j ):
                    d = d - (matrix[i][j]*x[j])
            x[i] = d/matrix[i][i]
        print(f'Iteration {iterations+1}:\n x = {x}')
    return x


A = np.array([[5,-2,-1,4],[-2,4,1,0],[1,2,6,-1],[-1,0,1,6]])
b = np.array([6,0,6,-14])

A,b = make_diagonal_dominant(A,b)

GaussSeidel(A,b,10)