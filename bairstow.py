from math import sqrt
from math import fabs


def cuadratica(c,b,a):
    x0 = 0+0j
    x1 = 0+0j
    disc = b**2-4*a*c

    if disc >= 0:
        val = sqrt(disc)
        x0 = (-b+val)/(2*a) + 0j
        x1 = (-b-val)/(2*a) + 0j
    else:
        val = sqrt(-disc)
        x0 = (-b+(val)*1j)/(2*a) #por qué no agarra la 'j'
        x1 = (-b-(val)*1j)/(2*a)
    return x0, x1

def bairstow(a,tol1, tol2, r0, s0, grado):
    b= []
    c = []
    roots = []
    for i in range(grado):
        b.append(0)
        c.append(0)
        roots.append(0 + 0j)
    b.append(0)
    c.append(0)

    iter = 0
    maxiter = 100
    while iter < maxiter and grado >= 3:
        e1 = e2 = 1
        r = r0
        s = s0

        while iter < maxiter and (e1 > tol1 or e2 > tol2):
            iter+=1
            b[grado] = a[grado]
            b[grado-1] = a[grado-1] + r*b[grado]

            c[grado] = b[grado]
            c[grado-1] = b[grado-1] + r*c[grado]

            for i in range(grado-2,-1,-1):
                b[i] = a[i] + r*b[i+1] + s*b[i+2]
                c[i] = b[i] + r * c[i + 1] + s * c[i + 2]


            #Resolver sistema de ecuaciones
            det = c[2]*c[2] -c[3]*c[1]
            if fabs(det) > tol1:
                dr = (-b[1]*c[2] + b[0]*c[3])/det
                ds = (-b[0] * c[2] + b[1] * c[1]) / det
                r = r+dr
                s = s+ds

                if fabs(r) > tol1:
                    e1 = fabs(dr/(r+dr))
                if fabs(s) > tol1:
                    e2 = fabs(ds/(s+ds))
            else:
                r+=1
                s+=1
                iter = 0

        c1, c2 = cuadratica(-s, -r, 1)
        roots[grado - 1] = c1
        roots[grado - 2] = c2
        grado -= 2

        for i in range(grado + 1):
            a[i] = b[i + 2]

    if grado<3:
        if grado ==2:
            c1,c2 = cuadratica(a[0], a[1], a[2])
            roots[0] = c1
            roots[1] = c2
        else:
            roots[0] = -a[0]/a[1]

    return roots

if __name__ == '__main__':
    ec = [6,11,6,1]
    #print(bairstow(ec, 0.001,0.001,-5,4,3))
    ec2 = [1,-1,0,0,-1,1]
    print(bairstow(ec2, 0.001, 0.001, -5, 4, 5))

