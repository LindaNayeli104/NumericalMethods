#Daniel Díaz López
#Oscar Fernández Moreno
#Linda Nayeli Abundis López

from math import fabs


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
    extraeLU(a, o,n)
    return a,o, False

def extraeLU(a,o,n):
    L =[]
    U =[]
    for i in range(n):
        L.append([])
        U.append([])
        for j in range(n):
            U[i].append(0)
            L[i].append(0)
    c = 0
    for i in range(n, 0, -1):
        for j in range(i):
            U[n - i][j + c] = a[n - i][j + c]
        c += 1
    # Ahora para L
    for i in range(n - 1, -1, -1):
        for j in range(i):
            L[i][j] = a[i][j]
        L[i][i] = 1

    Lf = open("mat.l.txt", "w")
    Lf.write(str(n))
    Lf.write("\n")
    for i in range(n):
        for j in range(n):
            Lf.write(str(L[i][j])+" ")
        Lf.write("\n")
    Lf.close()

    Uf = open("mat.u.txt", "w")
    Uf.write(str(n))
    Uf.write("\n")
    for i in range(n):
        for j in range(n):
            Uf.write(str(U[i][j])+" ")
        Uf.write('\n')
    Uf.close()

    of = open("mat.o.txt", "w")
    for i in range(n):
        of.write(str(o[i]) + " ")
    of.write("\n")
    of.close()

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




if __name__ == '__main__':
    a = [[1,4,-2],[3,-2,5],[2,3,1]]
    n = 3
    tol = 0.01
    b = [3,14,11]
    descompone(a,n,tol)
    #L = [[1, 0, 0], [1.5, 1, 0], [2, 3, 1]]
    #U = [[0.5, -0.384615, -1.153846], [0, -6.5, 3.5], [0, 0, 1]]
    #importaLU(L,U)

