import math



def f(x):
    '''to culculate the result.'''
    return math.sin(14/55)-27*math.pi+50*math.e*7/((x-6)*(x+10))-12*math.cos(x+8)+(x-14)**0.5



def domain(x):
    '''check if the entered value of x belongs to the domain of definition'''
    return x>=14



def answer(x):
    '''Calculates the answer using functions domain and f'''
    if domain(x):
        return f(x), True
    else:
        return None, False


def body():
    '''ask the user to enter the value for which he wants to calculate
    the function and check if it is possipble to float it'''
    try:
        x=input('enter the value for which you want to calculate the function')
        x=float(x)
    except (ValueError, EOFError, KeyboardInterrupt):
        return "wrong input"
    print("***** do calculations ...",end=" ")
    result=answer(x)
    print("done")
    print(f"for x={x:.8f}\n"
        "result=",end='')
    if result[1]:
        return f"{result[0]:.8f}"
    else:
        return "undefined"


print(
    "This is a program, which helps you calculate the result of the mathematical formula \n"
    "for a certain value of the variable parameter, variant 79")
print("Mykola Kolomiiets, K-12")
print(body())
