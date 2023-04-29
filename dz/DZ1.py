"""
1. Написати заголовок та задокументувати та реалізувати функцію, що
а) реалізує введення додатного дійсного числа користувачем;
б) приймає 2 дійсних параметри й повертає результат порівняння їх тангенсів;
в) за довжинами сторін трикутника повертає його площу.

2. Записати умову того, що змінні a,b, c позначають той самий об'єкт

3. Написати функцію, що задає умову того, що прямокутну цеглину з довжинами ребер a, b, c можна просунути в прямокутне
вікно x на y так, щоб її грані були паралельні сторонам вікна. Цеглину можна повертати.

4. Написати функцію, що повертає число в діапазоні [a, b]

5. Написати функцію, що обчислює деякий тригонометричний вираз

6. Модифікувати програму, яка запитує в користувача координати точки дійсної площини, а потім
виводить отриману точку, так, щоб вона не тільки використовувала функції, але ще обробляла
винятки.
1_2
"""
#1a
import math
def chislo():
    a=input('Введіть додатнє ціле число')

#1b
def comparetg(a,b):
    try:
        if  math.tan(a)<math.tan(b):
            return math.tan(b)
        else:
            return math.tan(a)
    except:
        print('one or both of the tan is not avalible')


#1v
def squer(a,b,c):
    p=(a+b+c)/2
    return (p(p-a)(p-b)(p-c))**0.5


#2
def comare(a,b,c):
    if a is b is c:
        print('ok')
    else:
        print('not ok')


#3
def zeglyna(a,b,c,x,y):
    if a<b:                                         #find the smallest values stm1 and stm2
        stm1=a
        if c<b:
            stm2=c
        else: stm2=b
    else:
        stm1=b
        if c<a:
            stm2=c
        else: stm2=a
    if x>=stm1 and y>=stm2:                          #compare them to know if it warks
        return True
    elif y>=stm1 and x>=stm2:
        return True
    else: return False

#4
def diapazon(a,b):
    c=(math.pi/3)**(a+b)
    while b>a:
        if b-a<c:
            c/=3
        else:
            return round(a+c,1)

def ctg(x):
    if x%180==0:
        print(eror)
    else:
        return float(math.sin(math.pi*x/180)/math.cos(math.pi*x/180),2)

def dot(a,b):
    try:
        c=float(a)
        c=float(b)
        print(a,b)
    except: print('type is not avelible')
    
