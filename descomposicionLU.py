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
        o[i] = i
        s[i] = i
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
                a[o[i]][j] = a[o[i]][j] - factor*a[o[k]][j]

    if(fabs(a[o[k]][k] / s[o[k]]) < tol):
        return a,o,False
    return a,o, False

def pivot(a,o,s,n,k):
    p = k
    big = fabs(a[o[k]][k] / s[o[k]])
    for i in range(k+1,n):
        dummy = fabs(a[o[i]][k] / s[o[i]])
        if(dummy > big):
            big = dummy
            p = i
    dummy = o[p]
    o[p] = o[k]
    o[k] = dummy
    return o,s

def solve(a,o,b,n):
    x = []
    for i in range(n):
        x[i] = 0
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