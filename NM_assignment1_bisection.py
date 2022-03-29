def fx_example(x):
    return x**2 - 3
    
def fx_q2(x):
    return x**6-x-1



def bisection(fx,a,b,iteration,stoppingcondition):

    # proceed to this condition when has stopping condition such as interval width 
    if(stoppingcondition is not None):
        while(True):
            c = (a+b)/2
            fc = fx(c)
            fa = fx(a)
            fb = fx(b)
            print(a, b, fa, fb, c, fc,b-a)

            if(abs(b-a)<= stoppingcondition):
                break

            if(fc == 0):
                return c
            elif(fc * fa < 0):
                b = c
            elif(fb * fc < 0):
                a = c
            
        return a if abs(fa) < abs(fb) else b

    else: #continue this condition when the process only based on number of iteration

        for i in range(iteration):
            c = (a+b)/2
            fc = fx(c)
            fa = fx(a)
            fb = fx(b)
            print(a, b, fa, fb, c, fc)

            if(fc == 0):
                return c
            elif(fc * fa < 0):
                b = c
            elif(fb * fc < 0):
                a = c

        return a if abs(fa) < abs(fb) else b


# test for question 1
# print(f"The root is = {bisection(fx_example,1,2,7,None)}")

# question 2
# print(f"The root is = {bisection(fx_q2,1,2,None,stoppingcondition=0.01)}")
    