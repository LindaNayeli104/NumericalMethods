import math


def biseccion(fun, x_l, x_r, tol):
    # x_l < x_r
    x_m = (x_r - x_l) / 2
    fm = fun(x_m)
    candidate = math.fabs(fm)
    while candidate > tol:               #tolerance 
        x_m = (x_r - x_l) / 2
        fm = fun(x_m)              #Evaluation of the function in the middle point
        candidate = math.fabs(fm)
        if candidate < tol:
            return x_m
        else:
            test = fun(x_l) * fm
            if test > 0:
                x_l = x_m # candidate = x_m
            else:
                x_r = x_m
    return x_m

"""
def f(x):
    return x**2 + x-6
"""
           
if __name__ == "__main__":
    # x^2 + x-6
    # root = biseccion(f,)
    root = biseccion(lambda x:(x**2 + x - 6), -1, 100, 0.0001)
    print(root)

