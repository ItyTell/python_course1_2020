"""
This program use 3 function to calculate the result of math formula
for the different values from the domain of definition and
with different accuracy(eps).
"""
a, b = -0.9, 0.9

def s(x,eps):
    """
    Just to culculate the value of funkcion.
    """
    q=0
    k=(x*x*x)/3
    n=1
    while k>eps or k<-eps:
        q+=k
        k=k*x*x*n*(2*n-1)/((n+1)*(2*n+3))
        n+=1
    return q

def Input_and_check():
    """
    Give 0 if values are not ok and x1, x2 if ok
    where x1=x and x2=eps.
    """
    try:
        x1 = float(input('enter the value for which you want to calculate the function'))
        x2 = float(input('enter epsilon'))
    except BaseException:
        return 0
    if x1>=a and x1<=b and x2>0:
        return x1,x2
    else:
        return 0


def body():
    """
    Ask the user to enter the value for which he wants to calculate
    the function and check if it is possipble to float it.
    """
    c = Input_and_check()
    if c==0:
        return "***** Error"   
    x = c[0]
    eps = c[1]
    print("***** do calculations ...",end=" ")
    result = s(x,eps)
    print("done")
    print(f"for x={x:.5f}")
    print(f"for eps={eps:.4E}\n"
        "result=", end='')
    return f"{result:.9f}"



print(
    "This is a program, which helps you calculate the result of the mathematical formula \n"
    "for a certain value of the variable parameter and with certain accuracy, variant 79")
print("Mykola Kolomiiets, K-12")
print(body())