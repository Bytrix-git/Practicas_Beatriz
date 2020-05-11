#!/usr/bin/env python3

import math
from os import system

# AÑADIR UNA EXCEPCION POR SI EL NUMERO ES MUY GRANDE Y DA ERROR

def Suma(vble):
    try:
        total=float(input("2º numero: "))
        total += vble
        return total                        #"{:.2f}".format(total)
    except:
        print("Tienes que introducir numeros")
  
def Resta(vble):
    try:
        var2=float(input("2º numero: "))
        vble -= var2
        return vble
    except:
        print("Tienes que introducir numeros")

def Mult(vble):
    try:
        total=float(input("2º numero: "))
        total *= vble
        return total
    except:
        print("Tienes que introducir numeros")
  
def Division(vble):
    try:
        var2=float(input("2º numero: "))
        vble /= var2
        return vble

    except ZeroDivisionError:
        print("No puedes dividir por cero")
    except:
        print("Tienes que introducir numeros")
  
def CambiaSigno(vble):
    try:
        return -vble
    except TypeError:#con string
        return "Debes introducir un numero!"
    except:
        return "Prueba de nuevo"

def TantoCiento(numTanto):
    try:
        var2= float(numTanto/100)
        return var2
    except TypeError:#con string
        return "Debes introducir un numero!"
    except:
        return "Prueba de nuevo"

def UnoEntreX(numX):
    try:
        var2=1/numX
        return var2
    except TypeError:#con string
        return "Debes introducir un numero!"
    except:
        return "Prueba de nuevo"

def xCuadrado(opCuad):
    try:
        var2=pow(vble, 2)
        return var2
    except TypeError: #al introducir un string
        return "Debes introducir un valor numérico!"
    except: 
        return "Prueba de nuevo"
    
def xElevadoY(vble):
    try:
        var2=float(input("2º numero: "))
        var2=pow(vble, var2)
        return var2
    except TypeError: #al introducir un string
        return "Debes introducir un valor numérico!"
    except: 
        return "Prueba de nuevo"


def xFactorial(opFact):               # Tiene que ser entero y positivo
    return math.factorial(opFact)
    
def raiz (opraiz):
    return math.sqrt(int(opraiz))

def Seno(opSeno):
    try:
        var2=math.sin(opSeno)
        return var2
    except TypeError: #al introducir un string
        return "Debes introducir un valor numérico!"
    except: 
        return "Prueba de nuevo"

def Coseno(opCos):
    try:
        var2=math.cos(opCos)
        return var2
    except TypeError: #al introducir un string
        return "Debes introducir un valor numérico!"
    except: 
        return "Prueba de nuevo"

def LogDiez(oplog):
    try:
        var2=math.log10(oplog)
        return var2
    except TypeError: #al introducir un string
        return "Debes introducir un valor numérico!"
    except: 
        return "Prueba de nuevo"





