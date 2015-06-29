#coding: utf8
def power_optimized(a,n):
    """
    1.1.4. Посчитать а в степени n за logn операций
    """
    b=1
    c=a
    k=n
    for i in range(n):
        if k%2==0:
            c=c*c
            k=k/2
        else:
            b=c*b
            k=k-1

        if k==0:
            return b
    return b

def div_mod(a,b):
    """
    1.1.7. Дано два числа, вычислить остаток и частное, не используя div и mod
    """
    c,d=a,b
    mod1=0
    div1=0
    while (c>d):
        div1=div1+1;
        c=c-d
    return (div1,c)

def fibo_logn(n):
    """
    1.1.10. Вычислить n-е число Фиббоначчи за logn
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    fn,fn1,f1n=1,1,0    #итоговая матрица
    sn,sn1,s1n=1,1,0    #матрица квадратов
    k = n
    count = 0;
    while k != 0:
        count = count + 1
        if k % 2 == 0:
            an1 = sn1 * sn1 + sn * sn
            an = sn1 * sn + sn * s1n
            a1n = sn * sn + s1n * s1n
            sn,sn1,s1n=an,an1,a1n
            k = k / 2
        else:
            an1 = fn1 * sn1 + fn * sn
            an = fn * sn1 + f1n * sn
            a1n = fn * sn + f1n * s1n
            fn,fn1,f1n = an,an1,a1n
            k = k - 1
    print count
    return fn

def factorial(n):
    if n < 2:
        return 1
    return factorial(n - 1) * n

def factor_sum(n):
    """
    1.1.11. Вычислить 1/0! + 1/1! + 1/2! ... + ... 1/n!
    """
    result = 0.0
    for i in range(n+1):
        print i
        result = result + 1.0 / factorial(i)
    return result

def factor_sum_optimized(n):
    """
    1.1.12. Вычислить 1/0! + 1/1! + 1/2! ... + ... 1/n! за n операций
    """
    if n == 0:
        return 1;
    if n == 1:
        return 2;

    factorial = 1;
    result = 2.0
    count = 0;

    for i in range(2, n + 1):
        count = count + 1
        factorial = factorial * i
        result = result + 1.0 / (factorial)

    print count
    return result

def euclide(m,n):
    if (m > n):
        a = m
        b = n
    else:
        a = n
        b = m
    r = a % b
    while r != 0:
        r = a % b
        if r != 0:
            a = b
            b = r
    return b

print euclide(119,544)
