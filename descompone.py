#Daniel Díaz López
from math import fabs
import gauss


def descomposicionLU(a,b,n,tol):
    a,o,error = descompone(a,n,tol)
    if not error:
        x = solve(a,o,b,n)
        return x
    else:
        return error

def descompone(a,n, tol):
    o = []
    s = []
    #Vamos a inicializar los arreglos
    for i in range(n):
        o.append(i)
        s.append(i)
    for i in range(n):
        s[i] = fabs(a[i][0])
        for j in range(1,n):
            dummy = fabs(a[i][j])
            if(dummy > s[i]):
                s[i] = dummy

    for k in range(n-1):
        o,s = pivot(a,o,s,n,k)
        if(fabs(a[o[k]][k]/s[o[k]])<tol):
            return a,o,True
        for i in range(k+1,n):
            factor = a[o[i]][k]/a[o[k]][k]
            a[o[i]][k] = factor
            for j in range(k+1,n):
                a[o[i]][j] -= factor*a[o[k]][j]

    if(fabs(a[o[k]][k] / s[o[k]]) < tol):
        return a,o,True
    return a,o, False

def pivot(a,o,s,n,k):
    p = k
    big = fabs(a[o[k]][k] / s[o[k]])
    i=0
    while k+i < n:
    #for i in range(k+1,n):
        dummy = fabs(a[o[i]][k] / s[o[i]])
        if(dummy > big):
            big = dummy
            p = i
        i+=1
    dummy = o[p]
    o[p] = o[k]
    o[k] = dummy
    return o,s

def solve(a,o,b,n):
    x = []
    for i in range(n):
        x.append(0)
    for i in range(1,n):
        accumulator = b[o[i]]
        for j in range(i):
            accumulator-= a[o[i]][j] * b[o[j]]
        b[o[i]] = accumulator
    x[n-1] = b[o[n-1]] / a[o[n-1]][n-1]
    for i in range(n-1,-1,-1):
        accumulator = 0
        for j in range(i+1,n):
            accumulator += a[o[i]][j] * x[j]
        x[i] = (b[o[i]] - accumulator) / a[o[i]][i]
    return x


def matrizU(a):
    u = []
    for i in range(len(a)):
        u.append([])
        for j in range(len(a[i])):
            u[i].append(0)

    #print(u)


    
    
            

    pass
    
if __name__ == "__main__":
    a = [[1,4,-2],[3,-2,5],[2,3,1]]
    n = 3
    tol = 0.01
    b = [3,14,11]
    u = []
    l = []
    a, b, c= descomposicionLU(a,b,n,tol)

    #matrizU(a)
    print(a)