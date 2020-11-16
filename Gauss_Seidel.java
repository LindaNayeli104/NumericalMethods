import math


def gauss_seidel(a, b, n, xInv, iMax, tol, relFac):
    x = []
    x = xInv
    for i in range(n):
        dummy = a[i][i] + 0.0
        if dummy > tol:
            for j in range(n):
                a[i][j] = a[i][j] / dummy
            b[i] = b[i]/dummy
        else:
            return "Error hay un cero en la diagonal"
    for i in range(n):
        suma = b[i]
        for j in range(n):
            if i != j:
                suma = suma - (a[i][j]*x[j])
        x[i] = suma
    itera = 0
    sentinel = True
    while sentinel == True and (itera < iMax):
        sentinel = False
        for i in range(n):
            old = x[i]
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma = suma - (a[i][j] * x[j])
            x[i] = relFac * suma+(1-relFac)*old
            if (sentinel == False and math.fabs(x[i]) > tol):
                ea = math.fabs((x[i] - old)/x[i])
                # ed no existe lo cambiamos por la tolerancia
                if ea > tol:
                    sentinel = True
        itera += 1
    return x


"""
Linda Nayeli
Oscar Fernandez
"""