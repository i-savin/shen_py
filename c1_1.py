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
        a = b
        b = r
    return

euclide(36,18)
