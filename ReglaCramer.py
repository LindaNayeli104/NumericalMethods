import os


def calcDets3x3(matriz3, res3):    
    detS = ((matriz3[0][0] * matriz3[1][1] * matriz3[2][2]) + (matriz3[1][0] * matriz3[2][1] * matriz3[0][2]) + (matriz3[2][0] * matriz3[0][1] * matriz3[1][2])) - ((matriz3[0][2] * matriz3[1][1] * matriz3[2][0]) + (matriz3[1][2] * matriz3[2][1] * matriz3[0][0]) + (matriz3[2][2] * matriz3[0][1] * matriz3[1][0]))

    detX = ((matriz3[0][3] * matriz3[1][1] * matriz3[2][2]) + (matriz3[0][1] * matriz3[1][2] * matriz3[2][3]) + (matriz3[0][2] * matriz3[1][3] * matriz3[2][1])) - ((matriz3[0][2] * matriz3[1][1] * matriz3[2][3]) + (matriz3[0][3] * matriz3[1][2] * matriz3[2][1]) + (matriz3[0][1] * matriz3[1][3] * matriz3[2][2]))

    detY = ((matriz3[0][0] * matriz3[1][3] * matriz3[2][2]) + (matriz3[1][0] * matriz3[2][3] * matriz3[0][2]) + (matriz3[2][0] * matriz3[0][3] * matriz3[1][2])) - ((matriz3[0][2] * matriz3[1][3] * matriz3[2][0]) + (matriz3[1][2] * matriz3[2][3] * matriz3[0][0]) + (matriz3[2][2] * matriz3[0][3] * matriz3[1][0]))

    detZ = ((matriz3[0][0] * matriz3[1][1] * matriz3[2][3]) + (matriz3[0][1] * matriz3[1][3] * matriz3[2][0]) + (matriz3[0][3] * matriz3[1][0] * matriz3[2][1])) - ((matriz3[0][3] * matriz3[1][1] * matriz3[2][0]) + (matriz3[0][0] * matriz3[1][3] * matriz3[2][1]) + (matriz3[0][1] * matriz3[1][0] * matriz3[2][3]))
    
    if(detS == 0.0):
        print("No tiene solución")
    else:
        x = detX / detS
        y = detY / detS
        z = detZ / detS

    res3[0] = x
    res3[1] = y
    res3[2] = z


def calcDets2x2(matriz2, res2):    
    detS = ((matriz2[0][0] * matriz2[1][1]) - (matriz2[0][1] * matriz2[1][0]))

    detX =  ((matriz2[0][2] * matriz2[1][1]) - (matriz2[0][1] * matriz2[1][2]))

    detY =  ((matriz2[0][0] * matriz2[1][2]) - (matriz2[0][2] * matriz2[1][0]))

    x = detX / detS
    y = detY / detS

    res2[0] = x
    res2[1] = y

if __name__ == '__main__':
    os.system("cls")

    matriz = [[0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]

    res = [0.0,0.0,0.0]

    matriz2 = [[0.0,0.0,0.0],[0.0,0.0,0.0]]
    matriz3 = [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    
    res2 = [0.0,0.0]
    res3 = [0.0,0.0,0.0]

    print("REGLA DE CRAMER")
    
    print("\nIngresa 2 si tu sistema de ecuaciones es de 2*2")
    print("Ingresa 3 si tu sistema de ecuaciones es de 3*3")
    ecuacionesNo = input("2 o 3: ")

    if(ecuacionesNo == "2"):
        print("\nA1x + B1y = D1")
        print("A2x + B2y = D2")

        print("\nSi tu ecuacion no cuenta con ese valor ingresa 0")

        print("\nIngrese valores:\n")

        matriz2[0][0] = float(input("Ingrese A1: "))
        matriz2[0][1] = float(input("Ingrese B1: "))
        matriz2[0][2] = float(input("Ingrese D1: "))

        matriz2[1][0] = float(input("\nIngrese A2: "))
        matriz2[1][1] = float(input("Ingrese B2: "))
        matriz2[1][2] = float(input("Ingrese D2: "))

        calcDets2x2(matriz2, res2)

        print("Los valores de las variables son x= " + str(res2[0]) + ", y= " + str(res2[1]))

    if(ecuacionesNo == "3"):
        print("\nA1x + B1y + C1z = D1")
        print("A2x + B2y + C2z = D2")
        print("A3x + B3y + C3z = D3")

        print("\nSi tu ecuacion no cuenta con ese valor ingresa 0")

        print("\nIngrese valores:\n")

        matriz3[0][0] = float(input("Ingrese A1: "))
        matriz3[0][1] = float(input("Ingrese B1: "))
        matriz3[0][2] = float(input("Ingrese C1: "))
        matriz3[0][3] = float(input("Ingrese D1: "))

        matriz3[1][0] = float(input("\nIngrese A2: "))
        matriz3[1][1] = float(input("Ingrese B2: "))
        matriz3[1][2] = float(input("Ingrese C2: "))
        matriz3[1][3] = float(input("Ingrese D2: "))

        matriz3[2][0] = float(input("\nIngrese A3: "))
        matriz3[2][1] = float(input("Ingrese B3: "))
        matriz3[2][2] = float(input("Ingrese C3: "))
        matriz3[2][3] = float(input("Ingrese D3: "))

        calcDets3x3(matriz3, res3)

        print("Los valores de las variables son x= " + str(res3[0]) + ", y= " + str(res3[1]) + ", z= " + str(res3[2]))
    else:
        print("Dato invalido")
    

    
   
    

    



     

 

