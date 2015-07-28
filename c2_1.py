#coding: utf8
def sequence(n, k):
    """
    2.1.1. Напечатать все последовательности длины k из чисел 1..n
    Ход решения - печатаем последовательности в лексикографическом порядке,
    например 111, 112, 113, 121, 122, 123, ... , 333.
    Т.е. инициализируем массив единицами и пока он не станет равным kk...k,
    печатаем следующую последовательность
    Для определения следующей последовательности используется функция next
    """
    x = [1 for i in range(k)]
    last = [n for i in range(k)]
    print x
    while x != last:
        x = next(x, n)
        print x

def next(x, n):
    p = len(x) - 1
    while x[p] == n:
        x[p] = 1
        p = p - 1
    x[p] = x[p] + 1
    return x

def sequence2(n, k):
    """
    Напечатать все последовательности длины k из чисел 0..n
    """
    x = [0 for i in range(k)]
    last = [n for i in range(k)]
    print x
    while x != last:
        x = next2(x, n)
        print x

def next2(x, n):
    p = len(x) - 1
    while x[p] == n:
        x[p] = 0
        p = p - 1
    x[p] = x[p] + 1
    return x

def subset(k):
    """
    2.1.3. Напечатать все подмножества множеств {1...k}
    Генерим все возможные последовательности 0 и 1 длины k и затем для индексов,
    значения в которых равно 1, выводим число
    """
    z = [i for i in range(1, k)]
    x = [0 for i in range(k)]
    last = [1 for i in range(k)]
    while x != last:
        x = next2(x, 1)
        y = []
        for i in range(k):
            if x[i] == 1:
                y.append(i + 1)
        print y

# sequence2(1, 5)
subset(3)
