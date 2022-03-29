import math

def fx_example(x):
    return x**2-2

def fx_q4(x):
    return x**4-5

def fx_q5(x):
    return math.exp(x)-(2-x)**3

def secant(fx,a,b,iteration):
    x_curr = b
    x_prev = a
    for i in range(1,iteration):
        x_new = x_curr - (((x_curr - x_prev)/(fx(x_curr)-fx(x_prev)))*fx(x_curr))
        print(i,x_prev,x_curr,fx(x_prev),fx(x_curr))

        x_prev = x_curr
        x_curr = x_new

    return x_curr

# test for question 3
# print(f"The root is = {secant(fx_example,1,1.5,4)}")

# question 4
# print(f"The root is = {secant(fx_q4,1,2,10)}")


# question 5
# print(f"The root is = {secant(fx_q5,0,5,10)}")
