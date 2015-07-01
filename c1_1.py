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

def euclide(a, b):
    """
    1.1.14. Алгоритмя Евклида с mod
    """
    if (a > b):
        m = a
        n = b
    else:
        m = b
        n = a
    r = m % n
    while r != 0:
        r = m % n
        if r != 0:
            m = n
            n = r
    return n

def euclide2(a, b):
    """
    1.1.13. Алгоритм Евклида без mod, только на вычитании
    """
    m, n = a, b
    while m != 0 and n != 0:
        if m > n:
            m = m - n
        else:
            n = n - m
    if m == 0:
        return n
    if n == 0:
        return m

def euclide3(a, b):
    """
    1.1.15. Даны a,b не равные нулю одновременно. Найти НОД d и такие целые числа x и y,
    что d = a * x + b * y. Не использовать деление с остатком
    """
    m, n, p, q, r, s = a, b, 1, 0, 0, 1
    # m = p * a + q * b
    # n = r * a + s * b
    while m != 0 and n != 0:
        if m > n:
            m = m - n
            p = p - r
            q = q - s
        else:
            n = n - m
            r = r - p
            s = s - q
    if m == 0:
        return [n, r, s]
    if n == 0:
        return [m, p, q]

def euclide4(a, b):
    """
    1.1.16. Даны a,b не равные нулю одновременно. Найти НОД d и такие целые числа x и y,
    что d = a * x + b * y. Использовать деление с остатком
    """
    m = a
    n = b

    p, q, r, s = 1, 0, 0, 1
    # m = p * a + q * b
    # n = r * a + s * b
    while m % n != 0:
        d = m % n
        t = m / n
        if d != 0:
            m = n
            n = d
            r1 = p - t * r
            s1 = q - t * s
            p = r
            q = s
            r = r1
            s = s1
    return [n, r, s]

def euclide5(a, b):
    """
    1.1.18. Даны a,b не равные нулю одновременно. Найти НОД d, не используя
    деление с остатком, а используя проверку четности деление пополам, а также
    соотношения НОД(2a,2b) = 2НОД(a,b) и НОД(2a,b) = НОД(a,b) для нечетного b
    """
    m, n, d = a, b, 1
    while m != 0 and n != 0:
        if m % 2 == 0 and n % 2 == 0:
            d = d * 2
            m = m / 2
            n = n / 2
        elif m % 2 == 0 and n % 2 != 0:
            m = m / 2
        elif m % 2 != 0 and n % 2 == 0:
            n = n / 2
        else:
            if m > n:
                m = m - n
            else:
                n = n - m
    if m == 0:
        return d * n
    else:
        return d * m

def square(n):
    """
    1.1.20. Вывести квадраты всех чисел от 0 до n
    """
    k = 0
    while k != n:
        print k * k
        k = k + 1

def square2(n):
    """
    1.1.21. Вывести квадраты всех чисел от 0 до n, но пользоваться можно только
    операциями сложения и вычитания, количество действий - n
    """
    print 0
    print 1
    k1 = 1
    k = 2
    # запишем квадрат следующего числа как квадрат суммы предыдущего числа и 1
    # (k_n)^2 = (k_n-1)^2 + k_n-1 + k_n-1 + 1
    while k != n:
        t = k1 + k - 1 + k - 1 + 1
        print t
        k1 = t
        k = k + 1

def factorization(n):
    """
    1.1.22 - 1.1.23. Разложить число на простые множители
    """
    a = n
    i = 2
    while i != a:
        if a % i == 0:
            a = a / i
            print i
            i = 2
        else:
            i = i + 1
        if i * i > n:
            break
    print a

def simplicity_test(n):
    """
    1.1.24. Проверить, является ли число простым
    """
    a = n
    i = 2
    while i * i <= a:
        if a % i == 0:
            return n, 'No'
        i = i + 1
    return n, 'Yes'

# print euclide3(119,544)
# print euclide4(119,544)
# print euclide3(6, 21)
# print euclide5(7, 21)
# square2(10)
# factorization(7399)
for i in range(100):
    print simplicity_test(i)
