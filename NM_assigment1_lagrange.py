import math

def x_value(n,i):
    return (10*i)/n - 5

def y_value(i): # the value return will be use as input for f(x)
    return (i/10) - 5

def y_function_a(x):
    return 1/(1+x**2)

def y_function_b(x):
    return math.sin(x)

def y_function_c(x):
    return (math.tan(x)+1)/(math.sin(x**2) + 2)


def lagrange(n,x,func):
    # print(f'Calculating for p{n}...')
    pn = 0
    for i in range(n+1):
        xi = x_value(n,i) #this is for multiplication the y[i] value after got L[i] polynomial, using f(x) function
        temp = 1

        for j in range(n+1): # lagrange iteration multiplication
            if(j != i ): 
                temp = temp * ( (x - x_value(n,j)) / (x_value(n,i) - (x_value(n,j))) ) 

        # print(f'this is function(x{i}) : {func(xi)}')
        pn = pn + (temp * func(xi))
        # print(f'this is pn : {pn}')
    return pn

n = [2,4,6,8,10,12,14,16]
max_err = 0
list_err = []

# to run all at once from 0-100 yi

for i in range(len(n)):
    print(f'calculating p{n[i]}...')

    for j in range(101):
        print(f'this is for i = {j}')
        x = y_value(j)
        ans = lagrange(n[i],x,y_function_a)
        error = abs(y_function_a(x) - ans)
        print(f'f({x}) = {y_function_a(x)}   p({x}) = {ans}      error = {error}\n')
        list_err.append(error)
        # print(f'Value for p{n[7]} with value x of {x} is = {ans} and the error with f({x}) is : {y_function_a(x)} - {ans} = {error}')
        if(error > max_err):
            max_err = error
    # print(f'Value for p{n[i]} with value x of {x} is = {lagrange(n[i],x,y_function_b)}')
    # print(f'Value for p{n[i]} with value x of {x} is = {lagrange(n[i],x,y_function_c)}')

print(f'max error is : {max_err}')
# print(f'list : {list_err}')



## here to do value testing using x value above


# n = 2
# x = y_value(2)
'''Question 6a'''
# ans = lagrange(n,x,y_function_a)
# print(f'Value for p{n} with value x of {x} is = {ans}')
# print(f'f({x}) : {y_function_a(x)}   p{n}({x}) : {ans} , hence the error is : {abs(y_function_a(x) - ans)}\n')


'''Question 6b'''
# ans = lagrange(n,x,y_function_b)
# print(f'Value for p{n} with value x of {x} is = {ans}')
# print(f'f({x}) : {y_function_b(x)}   p{n}({x}) : {ans} , hence the error is : {abs(y_function_b(x) - ans)}\n')


'''Question 6c'''
# ans = lagrange(n,x,y_function_c)
# print(f'Value for p{n} with value x of {x} is = {ans}')
# print(f'f({x}) : {y_function_c(x)}   p{n}({x}) : {ans} , hence the error is : {abs(y_function_c(x) - ans)}')