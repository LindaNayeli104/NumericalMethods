#Linda Nayeli Abundis Lopez A01636416
#Oscar Fernandez Moreno A07013362

def polinomio(points, b):
    n =len(points)
    lins = []
    for i in range(0,n-1):
        lins.append(getLineal(points[i][0]))
    pol =[0 for i in range(n)]
    pol[0] = b[0]
    for i in range(1,n):
        bu = b[i]
        listlin = [0 for i in range(i)]
        for j in range(0,i):
            listlin[j] = lins[j]
        p = getPolinomio(listlin)
        p = polCons(p, bu)
        m =len(p)
        for j in range(0,m):
            pol[j] = pol[j]+p[j]
    return pol

def multiplicaLineal(lineal,pol):
    res=[0 for i in range(0,len(pol)+1)]
    for i in range(0,len(pol)):
        res[i]=lineal[0]*pol[i]
    for i in range(0,len(pol)):
        res[i+1]+=lineal[1]*pol[i]
    return res


def polCons(pol,cons):
    res=[0 for i in range(0,len(pol))]
    for i in range(0,len(pol)):
        res[i]=cons*pol[i]
    return res

def getB(points):
    n=len(points)
    mat=[]
    for i in range(0,n):
        mat.append([])
        for j in range(0,n):
            mat[i].append(0)
    for i in range (0,n):
        mat[i][0]=points[i][1]
    for j in range(1,n):
        for i in range(0,n-j):
            right=mat[i][j-1]
            left = mat[i + 1][j-1]
            dist = points[i+j][0]-points[i][0]
            mat[i][j] = (left-right)/dist
    return mat[0]


def getPolinomio(mono):
    res=mono[0]
    for i in range(1,len(mono)):
        res=multiplicaLineal(mono[i],res)
    return res

def getLineal(n):
    res=[]
    res.append(-n)
    res.append(1)
    return res