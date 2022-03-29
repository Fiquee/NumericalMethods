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
    return (math.tan(x+1))/(math.sin(x**2) + 2)


def lagrange(n,x,func):
    print(f'Calculating for p{n}...')
    pn = 0
    for i in range(n+1):
        xi = x_value(n,i) #this is for multiplication the y[i] value after got L[i] polynomial, using f(x) function
        temp = 1

        for j in range(n+1): # lagrange iteration multiplication
            if(j != i ): 
                temp = temp * ( (x - x_value(n,j)) / (x_value(n,i) - (x_value(n,j))) ) 

        print(f'this is function(x{i}) : {func(xi)}')
        pn = pn + (temp * func(xi))
        print(f'this is pn : {pn}')
    return pn

n = [2,4,6,8,10,12,14,16]
x = y_value(100) #comment this if you want to run all for y0 - y100


# to run all at once from 0-100 yi

# for j in range(100):
#     x = y_value(j)
#     print(f'Value for p{n[0]} with value x of {x} is = {lagrange(n[0],x,y_function_a)}')
#     # print(f'Value for p{n[i]} with value x of {x} is = {lagrange(n[i],x,y_function_b)}')
#     # print(f'Value for p{n[i]} with value x of {x} is = {lagrange(n[i],x,y_function_c)}')



## here to do value testing using x value above

'''Question 6a'''
ans = lagrange(2,x,y_function_a)
print(f'Value for p{2} with value x of {x} is = {ans}')
print(f'f({x}) : {y_function_a(x)}   p{2}({x}) : {ans} , hence the error is : {abs(y_function_a(x) - ans)}\n')


'''Question 6b'''
# ans = lagrange(2,x,y_function_b)
# print(f'Value for p{2} with value x of {x} is = {ans}')
# print(f'f({x}) : {y_function_b(x)}   p{2}({x}) : {ans} , hence the error is : {abs(y_function_b(x) - ans)}\n')


'''Question 6c'''
# ans = lagrange(2,x,y_function_c)
# print(f'Value for p{2} with value x of {x} is = {ans}')
# print(f'f({x}) : {y_function_c(x)}   p{2}({x}) : {ans} , hence the error is : {abs(y_function_c(x) - ans)}')