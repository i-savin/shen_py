#coding: utf8
from random import randint

def null_array(n):
    """
    1.2.1. Заполнить массив нулями
    """
    a = [0 for i in range(n)]
    return a

def copy_array(a):
    """
    1.2.3. Не используя оператор присваивания для массивов, составить программу,
    эквивалентную оператору x:=y
    """
    b = [a[i] for i in range(len(a))]
    return b

def different(n):
    """
    1.2.6. Найти количество различных элементов массива за n^2 действий
    """
    a = [randint(0,n) for i in range(n)]
    b = null_array(n)
    l = 0
    print a
    for i in range(n):
        s = 0
        for j in range(n):
            if b[j] == a[i]:
                s = 1
                break
        if s == 0:
            b[l] = a[i]
            l = l + 1
    print sorted(a)
    print (l + 1)

def different2(n):
    """
    1.2.7. Найти количество различных элементов массива за nlogn действий
    """
    a = [randint(0,n) for i in range(n)]
    b = sorted(copy_array(a))
    print b
    k = 1
    for i in range(n - 1):
        if b[i] != b[i+1]:
            k = k + 1
    print k

different2(10)
