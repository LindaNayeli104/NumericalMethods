#Marlene Rodríguez Harms A00227347
#Linda Nayeli Abundis López A01636416
#Daniel Díaz López A01636706


import math
def gauss(a,b,n,tol):
    s = []
    for i in range(0,n):
        s.append(0)
    for i in range(0,n):
        s[i] = math.fabs(a[i][0])
        for j in range(1,n):
            test = math.fabs(a[i][j])
            if test>s[i]:
                s[i] = test
    aa,bb,error = eliminate(a,b,s,n,tol)
    if(error == False):
        x = substitute(aa,bb,n)
    return x

def eliminate(a, b, s, n, tol):
    for k in range(n - 1):
        (a, b, s) = pivot(a, b, s, n, k)
        if math.fabs(a[k][k] / s[k]) < tol:
            return a,b,True #error
        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k + 1, n):
                a[i][j] -= (factor * a[k][j])
            b[i] -= factor * b[k]

    if math.fabs(a[n - 1][n - 1] / s[n - 1]) < tol:
        return a,b,True #error
    return a, b, False


def pivot(a, b, s, n, k):
    p = k
    big = math.fabs((a[k][k] / s[k]))
    for i in range(k + 1, n):
        dummy = math.fabs(a[i][k] / s[i])
        if dummy > big:
            big = dummy
            p = i
    if p != k:
        for j in range(k, n):
            dummy = a[p][j]
            a[p][j] = a[k][j]
            a[k][j] = dummy
        dummy = b[p]
        b[p] = b[k]
        b[k] = dummy
        dummy = s[p]
        s[p] = s[k]
        s[k] = dummy
    return a, b, s


def substitute(a,b,n):
    x=[]
    for i in range(0,n):
        x.append(0)
    x[n-1] = b[n-1]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum = sum + a[i][j]*x[j]
        x[i] = (b[i] - sum)/a[i][i]
    return x

if __name__ == '__main__':
    n = 6
    #a = [[1, 2, -3],
    #     [2, -1, 1],
    #    [4, -1, 1]]

    #b = [19, 0, 8]

    a = [[1, 1, 1, 0, 0, 0],
         [0, -1, 0, 1, -1, 0],
         [0, 0, -1, 0, 0, 1],
         [0 ,0 ,0 ,0 ,1 , -1],
         [0, 10, -10, 0, -15, -5],
         [5, -10, 0, -20, 0, 0]]


    b = [0,0,0,0,0,200]

    tol = 0.01
    print(gauss(a,b,n,tol))