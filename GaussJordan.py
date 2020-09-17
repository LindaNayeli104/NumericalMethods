#Linda Abundis 
#Oscar Fernandez 

import math

def solve(a, b, s, n, tol):
    inv_a = []
    
    for i in range(n):
        a.append([])
        inv_a.append([])
        for j in range(n):
            a[i].append(0)
            inv_a[i].append(0)
   
    for k in range(n):
        if (a[k][k] / s[k]) < tol:            
            return x, inv_a, det, True      
        for i in range(n):
            if i != k:
                factor = a[i][k] / a[k][k]
                for j in range(n):
                    a[i][j] =  a[i][j] - (factor * a[k][j])    
                    inv_a[i][j] =  inv_a[i][j] - (factor * inv_a[k][j])   
                b[i] = b[i] - factor * b[k]
    if math.fabs(a[n-1][n-1] / s[n-1]) < tol:
        return x, inv_a, det, True  
    det = 1
    for k in range(n):
        det = det * a[k][k]
        b[k] = b[k] / a[k][k]
        for i in range(n):                                  
            inv_a[k][i] = inv_a[k][i] / a[k][k]
        a[k][k] = 1
    x = b
    return x, inv_a, det


def gauss_jordan(a, b, n, tol):
    s = []
    for i in range(n):
        s.append(0)
    for i in range(n):
        s[i] =  math.fabs(a[i][0])
        for j in range(1,n):
            test = math.fabs(a[i][j])
            if test > s[i]:
                s[i] = test
        x, inv_a, det = solve(a,b,s,n,tol)
    if(error == False):
        return x, inv_a, det, False 
                
