#Marlene Rodríguez Harms A00227347
#Linda Nayeli Abundis López A01636416
#Daniel Díaz López A01636706

import gauss
import tkinter.filedialog


def resolvercircuito():
    print("Bienvenido! Con este sft podras calcular las corrientes de tu circuito!")
    print(" ")
#Ahora el menú
    control = True
    while(control):
        print("---Menú---")
        print("1 - Leer archivo.")
        print("2 - Ingresar ecuaciones.")
        answer = input("Ingresa el número de la opción que desees: ")
        if (answer == '1'):
            file = tkinter.filedialog.askopenfilename()
            a,v,b,n = leerArchivo(file)
            solver(a,v,b,n)
            control = False
        elif (answer == '2'):
            a, v, b, n = ingresarDatos()
            solver(a,v,b,n)
            control = False
        else:
            print("Ingresa una opción válida")

def solver(a,v,b,n):
    tol = 0.001
    resultados = gauss.gauss(a, b, n, tol)
    for i in range(n):
        print(v[i] + " = " + str(resultados[i]))

def leerArchivo(file):
    f = open(file, "r")
    size = int(f.readline())
    # Vamos a leer la matriz
    matrix = []
    for i in range(size):
        matrix.append([])
        row = f.readline().split()
        # print(row)
        for j in range(size):
            matrix[i].append(int(row[j]))

    # Vamos a leer las variables
    variables = f.readline().split()
    row = f.readline().split()
    # Vamos a leer las constantes
    constantes = []
    for i in range(size):
        constantes.append(int(row[i]))
    # Cerramos el archivo.
    f.close()
    return matrix, variables, constantes, size

def ingresarDatos():
    #size = int(input("¿Cuántos variables?"))
    variables = input("Ingresa las variables: ").split()
    size = len(variables)
#Imprimimos el número de columnas necesario.
    print("Ingresa las ecuaciones en el orden indicado. Puedes agregar los espacios necesarios entre valores.")
    print(" |", end="")
    for i in range(size):
        print(variables[i] +" |", end="")
    print(" |Constantes|")
#Ahora capturamos la matriz
    matrix = []
    constantes = []
    for i in range(size):
        matrix.append(input("->").split())
        row = []
        for j in range(size):
            row.append((int(matrix[i][j])))
        constantes.append(int(matrix[i][size]))
        matrix[i] = row
    return matrix, variables, constantes, size

if __name__ == '__main__':
    #file = tkinter.filedialog.askopenfilename()
    #resolvercircuito(file)
    #print("A continuacion selecciona un archivo de texto...")
    #time.sleep(0.5)
    #file = tkinter.filedialog.askopenfilename()
    resolvercircuito()