#coding: utf8
from random import randint

def null_array(n):
    """
    1.2.1. Заполнить массив нулями
    """
    a = [0 for i in range(n)]
    print len(a)
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

def different3(n, k):
    """
    1.2.8. Найти количество различных элементов массива, содержащего 
        числа от 1 до k за k + n действий
    """
    a = [randint(1,k) for i in range(n)]
    print a
    b = null_array(k)
    l = 0
    for i in range(n):
        b[a[i] - 1] = b[a[i] - 1] + 1
    print b
    for i in range(k):
        if b[i] != 0:
            l = l + 1
    print sorted(a)
    print l


different3(10, 10)
