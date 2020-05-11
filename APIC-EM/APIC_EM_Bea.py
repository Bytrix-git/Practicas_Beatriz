#!/usr/bin/env python3
import requests
import json
import urllib3
from pprint import pprint
from funciones_apic import *
import os


try:
    while True:
        os.system("cls")
        print("                                                                BEATRIZ PEREZ PADILLA  ")
        print(" ")
        print("**************************************************************************************")
        print("********************************       APIC-EM        ********************************")
        print("********************** INTERACTUA CON LOS DISPOSITIVOS DE CISCO **********************")
        print("**************************************************************************************")
        print("     Elige la operacion que deseas realizar: ")
        print("     1 .. Mostrar listado de HOSTS")
        print("     2 .. Mostrar listado de DISPOSITIVOS DE RED ")
        print("     3 .. LOCALIZACIONES: Mostrar listado e Incluir nueva Localizacion")
        print(" ")
        print(" ---------------- Selecciona una opcion del menu o Enter para salir ------------------ ")
        print(" > ")
        opcion=input()
        url=""
        if opcion=="1":
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
            respHost=GET_Dispositivo(url)
            DictHost=IniciaTablaElem(respHost)
            SubMenuHost(respHost, DictHost)

        elif opcion=="2":
            url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
            respNetDev=GET_Dispositivo(url)
            DictNetDev=IniciaTablaElem(respNetDev)
            SubMenuNetDev(respNetDev, DictNetDev)

        elif opcion=="3":
            SubMenuLocaliz()

        else: 
            break
 
except KeyboardInterrupt:
    print("¡Hasta pronto!")
   
except:			
    print("Lo siento, algo ha salido mal...")