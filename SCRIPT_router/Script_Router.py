#!/usr/bin/env python3
from ncclient import manager
from pprint import pprint
from funciones_script import *
from os import system


try:
    while True:
        system("cls")
        print("                                                          BEATRIZ PEREZ PADILLA  ")
        print(" ")
        print("*********************************************************************************")
        print("**********************         Automatizacion        ****************************")
        print("********************** ROUTER CSR1000v MEDIANTE NETCONF *************************")
        print("*********************************************************************************")
        print("     Elige la operacion que deseas realizar: ")
        print("     1 .. Tabla de interfaces y sus direcciones")
        print("     2 .. Crear nueva Interfaz ")
        print("     3 .. Borrar Interfaz ")
        print("     4 .. Tabla routing: Interfaz salida y Red destino")
        print("     5 .. Modulos yang compatibles con nuestro router")  
        print("     6 .. Salir")
        print(" ")
        print(" ------- Selecciona una opcion del menu o cualquier otra tecla para salir ------- ")
        print(" > ")
        opcion=input()
        if opcion=="1":
            TablaInterfaces()
            input("\n\nPulsa Enter para continuar...")

        elif opcion=="2":
            NuevaIfzLoopback()

        elif opcion=="3":
            BorrarIfzLoopback()
        
        elif opcion=="4":
            TablaRouting()
        
        elif opcion=="5":
            peticionCapab()

        else:
            #m.close_session()
            break
 
except KeyboardInterrupt:
    print("¡Hasta pronto!")
   
except:			
    print("Lo siento, algo ha salido mal...")