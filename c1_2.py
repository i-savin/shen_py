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

def different(a):
    """
    1.2.6. Найти количество различных элементов массива за n^2 действий
    """
    n = len(a)
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
    print l

def different2(a):
    """
    1.2.7. Найти количество различных элементов массива за nlogn действий
    """
    n = len(a)
    b = sorted(copy_array(a))
    print a
    k = 1
    for i in range(n - 1):
        if b[i] != b[i+1]:
            k = k + 1
    print sorted(a)
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

def reverse_array(a):
    """
    1.2.10. Переставить элемента массива в обратном порядке, не используя
        дополнительный массив
    """
    for i in range(len(a) / 2):
        s = a[i]
        a[i] = a[len(a) - 1 - i]
        a[len(a) - 1 - i] = s
    return a

def reverse_section(m, n):
    """
    1.2.11. Дан массив целых чисел длины m+n. Он представляет собой соединение
    двух отрезков-подмассивов 0 - m, m+1 - n. Не используя дополнительных массивов,
    поменять местами эти два отрезка за m+n действий
    """
    a = [randint(0, 20) for i in range(m + n)]
    print a
    # меняем порядок на противоположный в первом отрезке
    for i in range(m / 2):
        s = a[i]
        a[i] = a[m - 1 - i]
        a[m - 1 - i] = s
    # меняем порядок на противоположный во втором отрезке
    for i in range(m, m + n / 2):
        s = a[i]
        a[i] = a[len(a) - 1 - i + m]
        a[len(a) - 1 - i + m] = s
    print a
    # меняем порядок на противоположный в получившемся массиве
    a = reverse_array(a)
    print a

def reverse_section2(m, n):
    """
    1.2.11. Дан массив целых чисел длины m+n. Он представляет собой соединение
    двух отрезков-подмассивов 0 - m, m+1 - n. Не используя дополнительных массивов,
    поменять местами эти два отрезка за m+n действий
    """
    a = [randint(0, 20) for i in range(m + n)]
    #TODO сделать через поворот круга

def polinom(a, x):
    """
    1.2.12. Коэффициенты многочлена лежат в массиве a. Вычислить значение этого
    многочлена в точке x: a[n]x^2 + ... + a[1]x + a[0]
    """
    n = len(a)
    b = a[n-1]
    k = 0;
    # схема Горнера
    while k != n-1:
        k = k + 1
        b = b * x + a[n-1-k]
    print b

def d_polinom(a, x):
    """
    1.2.12. Коэффициенты многочлена лежат в массиве a. Вычислить значение
    производной этого многочлена в точке x: a[n]x^2 + ... + a[1]x + a[0]
    """
    n = len(a)
    b = a[n-1]
    k = 0;
    # схема Горнера
    while k != n-2:
        k = k + 1
        b = b * x + a[n-1-k]
    print b

def mul_polinom(a, b):
    """
    1.2.15. В массивах a и b содержатся коэффициенты двух многочленов. Записать в массив
    c коэффициенты их произведения (элемент массива с индексом i соответствует
    коэффициенту при x в степени i)
    """
    c = null_array(len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] = c[i+j] + a[i] * b[j]
    print c

k = 10
n = 2
a = [randint(1,k) for i in range(n)]
b = [randint(1,k) for i in range(n)]
print a, b

# different(a)
# different2(a)
# different3(k, n)
# reverse_array(a)
# polinom(a, 2)
# d_polinom(a, 2)
mul_polinom(a, b)
