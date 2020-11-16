class Polinomio: 
    def __init__(self, coeficientes=[0]):
        self.coef = coeficientes
        self.grado = len(coeficientes)

    def getGrado(self):
        return self.grado

    def getCoeficientes(self, idx):
        return self.coef[idx]

    def multiplicaConstante(self, constante):
        return Polinomio([x * constante for x in self.coef])

    def aumentaCoeficiente(self, final = True):
        if(final):
            self.coef = self.coef.append(0)
            self.grado = self.grado + 1
        else:
            self.coef.insert(0,0)
       

        
    def multiplicaLineal(self, pol_lineal):
        nuevo_pol = []
        nuevo_grado = self.getGrado() + 1
        nuevo_pol = [0 for i in range(nuevo_grado + 1)]
        factor = pol_lineal.getCoeficientes(0)
        op1 = multiplicaConstante(factor)
        op1.aumentaCoeficiente(True)
        factor = pol_lineal.getCoeficiente(1)
        op2 = multiplicaConstante(factor)
        op2.aumentaCoeficiente(False)
        
        





if __name__ == "__main__":
    obj1 = Polinomio([1,2,3])
    print(obj1.getGrado())
    obj2 = Polinomio()
    print(obj2.getCoeficientes())