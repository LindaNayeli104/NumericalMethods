from math import fabs

def solve(a, b, s, n, tol):
    inv_a = []
    """
    for i in range(m):
        inv_a.append([])
        for j in range(n):
            inv_a[i].append(0)
    """
    for i in range(0,n):
        for j in range(0,n):
            inv_a[i][j].append(0)
            if i==j:
               inv_a[i][j].append(1) 
    for k in range(0,n):
        if (a[k][k] / s[k]) < tol:                #Checar
            return "Error"
        for i in range(0,n):
            if i != 0:
                factor = a[i][k] / a[k][k]
                for j in range(0, n):
                    a[i][j] =  a[i][j] - factor *a[k][j]    
                    inv_a[i][j] =  inv_a[i][j] - factor *a[k][j]   
                b[i] = b[i] - factor * b[k]
    if fabs(a[n-1][n-1] / s[n-1]) < tol:
        return "Error"
    det = 1
    for k in range(0,n):
        det = det * a[k][k]
        b[k] = b[k] / a[k][k]
        for i in range(0,m):
            inv_a[k][i] = inv_a[k][i] / a[k][k]
        a[k][k] = 1
    x = b
    return x, inv_a, det


    def gauss_jordan(a, b, n, tol):
        s = []
        for i in range(0,n):
            s[i] = 0
        for i in range(0,n):
            s[i] =  fabs(a[i][0])
            for j in range(1,n):
                test = fabs(a[i][0])
                if test > s[i]:
                    s[i] = test
        try:
            x, inv_a, det = solve(a,b,s,n,tol)
        except:
            return x, inv_a, det
                
