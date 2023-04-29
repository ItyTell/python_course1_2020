"""
1. Написати код, який виконує такі дії.
Утворити об’єкт списка, що зберігає послідовність 1, 5, 87, 32.
Замінити елемент списка з індексом 1 на число 13.
Додати в кінець списка число 25.
Замінити елемент списка з індексом 1 на послідовність 4, 5.
Вирізати з списка елементи з індексами 3, 4.
Вставити в позицію з індексом 2 число 8.
Побудувати за списком кортеж.
Вивести кортеж.
Додати в кінець списка елементи кортежу.
Вилучити останній елемент списку.
Вивести список.
Вивести кортеж у зворотному порядку.


8. Написати функцію, що утворює новий список та заповнює його цілими числами з клавіатури.
а) Завершення введення відбувається тоді, коли чергове значення не може бути перетворено на тип цілих
або користувач натисне Ctrl-C.
б) Завершення введення відбувається тоді, коли користувач натисне Ctrl-C. Якщо чергове значення не
може бути перетворено на тип цілих введення вважається неуспішним та повертається None.
в) Попередня задача, але за неуспішного введення генерується виняток типу RuntimeError.
г) Та сама задача, але за Ctrl-C введення завершується, а введення нечислових даних ігноруються.
9. Написати функцію, що заповнює вже існуючий список цілими числами з клавіатури.



18. Написати функцію, що з списку цілих вилучає усі нульові елементи.
19. Написати функцію, що циклічно зсуває список на одну позицію вправо.


Написати функцію, яка утворює новий список і заповнює його послідовними біномними
коефіцієнтами C(n,k)
(k=0,1,..,n).
"""


a = [1, 5, 87, 32]
a[1]=13
a.append(25)
a.insert(1, 4)
a.insert(2, 5)
a.pop(3)
a.pop(4)
a.insert(2, 8)
b=(a[0],a[1],a[2],a[3],a[4],a[5])
print(b)
a.extend(b)
a.pop()
print(a)
c=[b[0],b[1],b[2],b[3],b[4],b[5]]
c.reverse()
print(c)
def list():
    list=[None]
    i=0
    while 1:
        try:
            x=y=input()
            x=float(x)
            list.append(y)
        except (ValueError,KeyboardInterrupt):
            return list




def list2():
    list=[None]
    i=0
    while 1:
        try:
            x=y=input()
            x=int(x)
            list.append(y)
        except KeyboardInterrupt:
            return list
        except ValueError:
            return None

def list3():
    list=[None]
    i=0
    while 1:
        try:
            x=y=input()
            x=int(x)
            list.append(y)
        except KeyboardInterrupt:
            return list
        except ValueError:
            raise RuntimeError




def list4():
    list=[None]
    i=0
    while 1:
        try:
            y=input()
            list.append(y)
        except KeyboardInterrupt:
            return list

def list_exist(a):
    i=0
    while 1:
        try:
            a.append(input())
        except BaseException:
            return a


def not_zero(a):
    while 1:
        try:
            a.remove(0)
        except ValueError:
            return a
import math

def Binom(n):
    k=1
    a.append(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))
    while k < n:
        k+=1
        a.append(a[k-2]*(n-k+1)/k)
    a.append(1)
    return a