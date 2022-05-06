import numpy as np


def make_diagonal_dominant(matrix, b):
    max_col_index = np.argmax(np.abs(matrix), axis=0)
    matrix = matrix[max_col_index]
    b = b[max_col_index]

    return matrix, b

def GaussSeidel(matrix,b,iteration,x=None):

    if x is None:
        x = np.zeros(len(matrix[0]))

    print(x)

    for iterations in range(iteration):
        for i in range(len(matrix[0])):
            d = b[i]

            for j in range(len(matrix[0])):
                if( i != j ):
                    d = d - (matrix[i][j]*x[j])
            x[i] = d/matrix[i][i]
        print(f'Iteration {iterations+1}:\n x = {x}')
    return x

def GaussSeidel_v(matrix,b,iteration,x=None): #Using vector style
    if x is None:
        x = np.zeros(len(matrix[0]))
    print(x)

    D = np.diag(matrix)
    R = matrix - np.diagflat(D)

    for i in range(iteration):

        for j in range(len(matrix[0])):
            x[j] = (b[j] - np.dot(R[j],x)) / D[j]

        print(f'Iteration {i+1}: \n x = {x}')
    
    return x



A = np.array([[5,1,2],[1,4,1],[2,2,5]])
b = np.array([1,2,3])

# A = np.array([[1,-5], [7,-1]])
# b = np.array([-4,6])


A,b = make_diagonal_dominant(A,b)
print(A)

# GaussSeidel(A,b,10)
print()
print()
GaussSeidel_v(A,b,3,[1,1,1])