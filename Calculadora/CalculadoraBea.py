from funciones_Calcu import *
from math import pi
from time import sleep
from os import system

#Menu con  la calculadora, con lista y exepciones
    
global vble
global mem
global menu
global listaNum
vble=0
listaNum=[]
mem=0
menu=0

try:
    system("cls")          
    while True:
        print("                                    BEATRIZ PEREZ PADILLA\n  ")
        print("    *****************************************************    ")
        print("    *************    CALCULADORA Python    **************    ")
        print("    -----------------------------------------------------    ")
        print("    -- INSTRUCCIONES:                                  -- ")
        print("    --       * Pulsa C para comenzar y para borrar     --")
        print("    --       * Pulsa CTRL+C para salir                 --")
        print("    -----------------------------------------------------    ")
        print("\n     MEM = ", mem, "                 TOTAL =   ", "{:.2f}".format(vble))
        print("      __________________________________________________ ")
        print("     |     C    |    +    |    -    |    *    |    /    |")
        print("     |    +/-   |    %    |   1/x   | (x2)x^2 |(xy)x^y  |")
        print("     |    n!    | (R)raiz |   sin   |   cos   |   log   |")
        print("     |    PI    |    M    |    M+   |    M-   |    MC   |")
        print("     |__________________________________________________| ")
        print(2*"\n")
        print("  ",end="Operacion: ")
        menu=input()
        print("\n")

#Introducir un número
        if menu=="C":
            vble = float(input("  Introduce un Número: "))
            system("cls")

#Funcion Sumar            
        if menu=="+":
            print(float(vble), end=" + ")
            vble=Suma(vble)
            system("cls")

#Funcion Restar 
        if menu=="-":
            print(float(vble), end=" - ")
            vble=Resta(vble)
            system("cls")

#Funcion Multiplicar             
        if menu=="*":
            print(float(vble), end=" * ")
            vble=Mult(vble)
            system("cls")

#Funcion Dividir 
        if menu=="/":
            print(float(vble), end=" / ")
            vble=Division(vble)
            system("cls")

#Funcion Cambio de signo 
        if menu=="+/-":
            print("+/-", float(vble), end=" ")
            vble=CambiaSigno(float(vble))
            system("cls")

#Funcion Tanto por Ciento 
        if menu=="%":
            print("%", float(vble), end=" ")
            vble=TantoCiento(float(vble))
            system("cls")

#Funcion 1/x             
        if menu=="1/x":
            print("1/", float(vble), end=" ")
            vble=UnoEntreX(float(vble))
            system("cls")

#Funcion x^2 
        if menu=="x2":
            print("x^2", float(vble), end=" ")
            vble=xCuadrado(vble)
            system("cls")

#Funcion x^y            
        if menu=="xy":
            print(float(vble), end=" ^ ")
            vble=xElevadoY(float(vble))
            system("cls")

#Funcion Factorial
        if menu=="n!":          # Tiene que ser entero y positivo
            print(float(vble), end="! ")             
            try:
                vble=xFactorial(vble)
            except ValueError: #al introducir un string
                input("Debes introducir un entero positivo!")
            except:
                input( "Prueba de nuevo")
            #system("cls")

#Funcion Raiz            
        if menu=="R":
            print("raiz (", float(vble), end=") ")
            try:
                vble=raiz(vble)
            except ValueError:#con valor negativo
                input("Debes introducir un entero positivo!")
            except:
                input( "Prueba de nuevo")

#Funcion Seno            
        if menu=="sin":
            print("seno (", float(vble), end=") ")
            vble=Seno(vble)
            system("cls")

#Funcion Coseno            
        if menu=="cos":
            print("coseno (", float(vble), end=") ")
            vble=Coseno(vble)
            system("cls")

#Funcion Log            
        if menu=="log":
            print("log (", float(vble), end=") ")
            vble=LogDiez(vble)
            system("cls")

#Funcion PI            
        if menu=="PI":
            vble= pi
            print("nº PI: ", vble)
            system("cls")
            
#Funcion Mostrar Memoria 
        if menu=="M":
            vble=mem
            system("cls")

#Funcion Sumar a memoria            
        if menu=="M+":
            mem += vble
            system("cls")
            print("Guardando...", mem)
            #system("cls")

#Funcion Restar de memoria            
        if menu=="M-":
            mem -= vble
            print("Guardando...", mem)
            #system("cls")

#Funcion Borrado de Memoria            
        if menu=="MC":
            mem=0
            print("Memoria eliminada...")
            system("cls")
        
        else:
            system("cls")

except KeyboardInterrupt:    #Ctrl+C: KeyboardInterrupt 
    print("\n¡Hasta pronto!")
   
except:			
    print("\nLo siento, algo ha salido mal...")


