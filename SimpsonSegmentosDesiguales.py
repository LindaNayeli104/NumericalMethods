import os

def sim38(h, f0, f1, f2, f3):
    return (3/8) * h * (f0 + 3 * f1 + 3 * f2 + f3)

def sim13mul(h, f0, f1, f2):
    sum = f0 + 4 * f1 + f2
    return (h/3) * sum

def trapecio(h, x, y):
    return ((h / 2) * (x + y))

def segDesiguales(n, x, f):
    h = x[1] - x[0]
    k = 1
    sum = 0
    for i in range(1, n):
        hf = x[i+1] - x[i]
        if(abs(h - hf) < 0.000001):
            if(k == 3):
                sum = sum + sim38(h, f[i-3], f[i-2], f[i-1], f[i])
                k = k - 2
            else:
                k = k + 1
        else:
            if(k == 1):
                sum = sum + trapecio(h, f[i-1], f[i])
            else:
                if(k == 2):
                    sum = sum + sim13mul(h, f[i-2], f[i-1], f[i])
                else:
                    sum = sum + sim38(h, f[i-3], f[i-2], f[i-1], f[i])
                k = 1
        h = hf
    if(k==3):
        sum = sum + sim38(h, f[i-2], f[i-1], f[i], f[i+1])
    if(k==2):
        sum = sum + sim13mul(h, f[i-1], f[i], f[i+1])
    if(k==1):
        sum = sum + trapecio(h, f[i], f[i+1])
    return sum

if __name__ == "__main__":
    os.system("cls")

    print("Metodo de integracion de segmentos desiguales combinando Simpson 1/3, 3/8 y Trapecio")
        
    print("\nIngrese valores:\n")
    
    n = int(input("Ingrese el numero de segmentos:  "))
 
    x = [i for i in range(n+1)]
    for i in range(n+1):
       x[i] = float(input("Ingrese el punto " + str(i+1) + ": ")) 

    f = [i for i in range(n+1)]
    for i in range(n+1):
       f[i] = float(input("Ingrese la evaluacion en el punto " + str(i+1) + ": ")) 
    
    result = segDesiguales(n, x, f)
    print("La respuesta es: " + str(result))

    """
    x = [0.0, 0.12, 0.22, 0.32, 0.36, 0.40, 0.44, 0.54, 0.64, 0.70, 0.80]
    f = [0.200000, 1.309729, 1.305241, 1.743393, 2.074903, 2.456000, 2.842985, 3.507297, 3.181929, 2.363000, 0.232000]
    n=10
    result = segDesiguales(n, x, f)
    print("La respuesta es: " + str(result))
    """