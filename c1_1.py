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

print fibo_logn(1000)
