import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No es posible dividir por cero"

def potencia(a, b):
    return a ** b

def radicacion(a, b):
    return a ** (1 / b)

def factorial(n):
    return math.factorial(n)

def logaritmo_base10(x):
    return math.log10(x)

def logaritmo_natural(x):
    return math.log(x)

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def arco_seno(x):
    return math.asin(x)

def arco_coseno(x):
    return math.acos(x)

def arco_tangente(x):
    return math.atan(x)

def exponencial(x):
    return math.exp(x)

def valor_absoluto(x):
    return abs(x)

def redondear(x):
    return round(x)

