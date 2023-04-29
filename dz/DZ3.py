"""
#прогак12

файл12. 14(в) 15 20 25
"""


def f(n):
    k=1
    a=[]
    a.append(1)
    while k<n:
        a.append(a[k-1]*(n+k)/k)
        k+=1
    print(a)


import math
def c(n):
    if n==1:
        return math.cos(n)
    else:
        return math.cos(n)+c(n-1)
def s(n):
    if n==1:
        return math.sin(n)
    else:
        return math.sin(n)+s(n-1)
def main(n):
    if n==1:
        return math.cos(n)/math.sin(n)
    else:
        return math.cos(n)/math.sin(n)+main(n-1)

def tapl(a,b,h,m):
    k=0
    for i in range(a,b,h):
        k+=1
        if k%m==0:
            x=input("Prodovzuemo?")
            if x==0:
                break
        print(math.sin(i))




def g():
    x=input("sin or cos?")
    if x=="sin":
        y=float(input("enter a number"))
        try:
            print(math.sin(y))
            g()
        except ValueError:
            print("error")
    if x=="cos":
        y=float(input("enter a number"))
        try:
            print(math.cos(y))
            g()
        except ValueError:
            print("error")







