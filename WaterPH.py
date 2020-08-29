#Linda Abundis 
#A01636416
import math

def biseccion(fun, x_lower, x_upper, tolerance):
    fun_lower = fun(x_lower)
    candidate = x_upper
    prev = x_lower
    while math.fabs(candidate - prev) > tolerance:
        candidate = (x_upper + x_lower) / 2.0
        fun_upper = fun(candidate)
        test = fun_lower * fun_upper
        if math.fabs(test) < tolerance:
            prev = candidate
        elif test < 0:
            x_upper = candidate
        else:
            x_lower = candidate
            fun_lower = fun_upper
    return candidate

def getH(pCO, h):
    k1 = 10**(-6.3)
    k2 = 10**(-10.3)
    kH = 10**(-1.4)
    kW = 10**(-14)
    return h*3 - (((k1*kH*pCO) / 10**6) + kW)*h - ((2*k1*k2*kH*pCO)/10**6)


if __name__ == "__main__":
    print("Get your water PH!")
    print("Introduce the next values")

    pCO = float(input("pCO: "))
    x_lower = float(input("lower limit: "))
    x_upper = float(input("upper limit: "))
    tolerance = float(input("tolerance: "))

    #h = biseccion(lambda h: getH(1958, h), 0.000001, 0.00001, 0.000001)   #Pruebas H= 5.2596
    h = biseccion(lambda h: getH(pCO, h), x_lower, x_upper, tolerance)
    pH = -1 * (math.log10(h))
    print(pH)


    