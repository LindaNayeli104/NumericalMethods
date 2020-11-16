import os


def sim38(h, f0, f1, f2, f3):
    return (3/8) * h * (f0 + 3 * f1 + 3 * f2 + f3)

def sim13mul(h, n, f):
    sum = f[0]
    for i in range(1, n-1, 2):
        sum = sum + 4 * f[i] + 2 * f[i+1]
    sum = sum + 4 * f[n-1] + f[n]
    return (h/3) * sum

def intsim(a, b, n, f):
    h = (b-a) / n
    sum = 0
    if(n == 1):
        sum = (h / 2) * (f[n-1] + f[n])
    else:
        m = n
        odd = n % 2    
        if(odd > 0 and n > 1):
            sum = sum + sim38(h, f[n-3], f[n-2], f[n-1], f[n])
            m = n-3
        if(m > 1):
            sum = sum + sim13mul(h, m, f)
    return sum

if __name__ == "__main__":
    os.system("cls")

    

    print("Metodo de integracion de segmentos iguales combinando Simpson 1/3 y 3/8")
        
    print("\nIngrese valores:\n")

    a = float(input("Ingrese el limite inferior del intervalo: "))
    b = float(input("Ingrese el limite superior del intervalo: "))
    n = int(input("Ingrese el numero de segmentos: "))
    
    f = [i for i in range(n+1)]

    for i in range(n+1):
       f[i] = float(input("Ingrese la evaluacion " + str(i+1) + ": ")) 
    #f = [-3375, -636.056, -10.648, 74.088, 1191.02, 4913]

    sum = intsim(a, b, n, f)
    print("El calculo de la integral da: " + str(sum))


