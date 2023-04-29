"""

13. Написати функцію, що утворює новий список та записує в нього n різних цілих чисел, що їх вводить
користувач. Число n є параметром функції. За неуспішного введення має генеруватися виняток
типу RuntimeError.

18. Написати функцію, що з списку цілих вилучає усі нульові елементи.



50. Рядок містить слова, відокремлені білими символами. Знайти кількість слів у рядку.
51. Попередня задача, але рядок дуже довгий та створювати копію навіть одного його слова не можна.
52. Попередня задача, але роздільниками слів є білі символи та знаки пунктуації (.,;:!?).
"""

def strochechka():
    a=[]
    while True:
        try:
            a.append(int(input('vedit')))
        except BaseException:
            raise RuntimeError

def ne_noll(a):
    x=0
    for i in range(len(a)):
        if a[i+x]==0:
            del(a[i+x])
            x+=1
    print(a)

def riadok(s):
    i=x=z=0
    while i < len(s):
        if s[i].isspace() and z==1:
            x+=1
            z=0
        elif not s[i].isspace():
            z=1
        i+=1
    return x-1




def riadok2(s):
    i=x=z=0
    while i < len(s):
        if s[i]==',' and z==1:
            x+=1
            z=0
        elif not s[i]==',':
            z=1
        i+=1
    return x-1
