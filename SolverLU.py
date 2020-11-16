#Daniel Díaz López
#Oscar Fernández Moreno
#Linda Nayeli Abundis López

L = [[1, 0, 0], [1.5, 1, 0], [2, 3, 1]]
U = [[0.5, -0.384615, -1.153846], [0, -6.5, 3.5], [0, 0, 1]]

def resuelve(L,U,o):
    L,U,o,n = leerArchivos(L,U,o)
    a = uneLU(L,U)
    coeficientes = input("Ingresa la matriz de coeficientes: ").split()
    b = []
    for i in range(n):
        b.append(float(coeficientes[i]))

    print(solve(a,o,b,n))

def leerArchivos(Lf,Uf,of):
    Lfi = open(Lf, "r")
    n = int(Lfi.readline())
    Lfi.close()
    L = []
    U = []
    o = []
    for i in range(n):
        L.append([])
        U.append([])
        o.append(0)
        for j in range(n):
            U[i].append(0)
            L[i].append(0)

    #Leemos los archivos
    Lfi = open(Lf, "r")
    Ufi = open(Uf, "r")
    ofi = open(of,"r")
    rowO = ofi.readline().split()
    Lfi.readline()
    Ufi.readline()
    for i in range(n):
        rowL = Lfi.readline().split()
        rowU = Ufi.readline().split()
        o[i] = int(rowO[i])
        for j in range(n):
            L[i][j] = float(rowL[j])
            U[i][j] = float(rowU[j])
    Lfi.close()
    Ufi.close()
    ofi.close()
    return L, U,o,n

def uneLU(L,U):
    n = len(L)
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    c = 0
    for i in range(n,0,-1):
        for j in range(i):
            a[n-i][j+c] = U[n-i][j+c]
        c+=1
    #Ahora integramos L
    for i in range(n-1,-1,-1):
        for j in range(i):
            a[i][j] = L[i][j]
    return a

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

if __name__ == '__main__':
    resuelve("mat.l.txt","mat.u.txt","mat.o.txt")