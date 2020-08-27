#import math              math.exp(i)
from math import exp as e

def fac(x):
    if x <= 1:
        return 1
    else:
        val = fac(x-1)
        val *= x                 #val = val * x
        return val

# def fac(x):
    #return 1 if x <= 1 else x*fac(x-1)              #Equivalente a operadores ternaros en Java

def serie(x):
    limit = 21
    acu = 1 + x
    for i in range(2,limit):
        acu += x**i / fac(i)
    return acu


if __name__ == '__main__':
    for i in range(1,11):
        valor_a = serie(i)
        valor_r = e(i)
        e_v = valor_r - valor_a
        print("Valor real: " + str(valor_r) + "\nValor aprox: " + str(valor_a) + "\nError verdadero: " + str(e_v))

