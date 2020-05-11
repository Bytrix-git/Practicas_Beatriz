# #!/usr/bin/env python3
import requests
import json
import urllib3
from pprint import pprint
from tabulate import *
import os

global ticket
global IdPeticion

requests.packages.urllib3.disable_warnings()

### SOLICITUD DEL TICKET DE FORMA GLOBAL PARA QUE SOLO SE EJECUTE UNA VEZ ###
urltick = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
headerstick = {
    "Content-type" : "application/json"
}
body_json = {
    "password": "Xj3BDqbU",
    "username": "devnetuser"
}

resptick = requests.post(urltick,json.dumps(body_json),headers=headerstick,verify=False)
responsetick_json=resptick.json()
ticket = responsetick_json ['response']['serviceTicket']

### PETICION GENERICA DE GET DE LA URL DEL APIC-EM ###
def GET_Dispositivo(url):
    headers = {
        "Content-type" : "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(url,headers=headers,verify=False)

    if resp.status_code != 200:
        raise Exception("El codigo de estado no es 200. Texto Respuesta: " + resp.text)

    resHosts_json=resp.json()
    return resHosts_json

### SUBMENU PARA ELEGIR DEL LISTADO DE HOSTS LOS ELEMENTOS QUE QUEREMOS MOSTRAR EN UNA TABLA ###
def SubMenuHost(respHosts, DictMostrar):
    elemen="hostIp"
    while True:
        os.system("cls")
        print("\n********************  SUB-MENU HOSTS  *******************")
        print("***********************************************************\n\n")
        print("   PUEDES AÑADIR LAS SIGUIENTES OPCIONES A LA TABLA PARA MOSTRAR\n:")
        print("     1 - Tipo de Cableado")
        print("     2 - ID de Vlan")
        print("     3 - MAC del host")
        print("     4 - Direccion del Dispositivo conectado")
        print("     5 - Nombre de la interfaz")
        print("     6 - Nombre del AP conectado")
        print("     7 - Ultima actualizacion")
        print(" ")
        print("    Pulsa cualquier otra tecla para Volver al menu PPAL")
        print(" ********************************************************** ")
        DictMostrar = Mostrar(respHosts, DictMostrar,elemen)
        print(" > ")
        opcion2=input()
        os.system("cls")
        if opcion2=="1": elemen="hostType"
        elif opcion2=="2": elemen="vlanId" 
        elif opcion2=="3": elemen="hostMac"        
        elif opcion2=="4": elemen="connectedNetworkDeviceIpAddress"
        elif opcion2=="5": elemen="connectedInterfaceName"
        elif opcion2=="6": elemen="connectedAPName"    
        elif opcion2=="7": elemen="lastUpdated"        
        else:
            break
    return

### SUBMENU PARA ELEGIR DEL LISTADO DE DISPOSITIVOS DE RED LOS ELEMENTOS QUE QUEREMOS MOSTRAR EN UNA TABLA ###
def SubMenuNetDev(respNetDev, DictMostrar):
    elemen="hostname"
    while True:
        os.system("cls")
        print("\n**************  SUB-MENU DISPOSITIVOS DE RED  *************")
        print("***********************************************************\n\n")
        print("   PUEDES AÑADIR LAS SIGUIENTES OPCIONES A LA TABLA PARA MOSTRAR\n:")
        print("     1 - Familia del Dispositivo")
        print("     2 - IP de gestión")
        print("     3 - Direccion MAC ")
        print("     4 - Nombre de la interfaz")
        print("     5 - Nombre del AP conectado")
        print("     6 - Ultima actualizacion")
        print(" ")
        print("    Pulsa cualquier otra tecla para Volver al menu PPAL")
        print(" ********************************************************** ")
        DictMostrar = Mostrar(respNetDev, DictMostrar,elemen)
        print(" > ")
        opcion2=input()
        os.system("cls")
        if opcion2=="1": elemen="family"
        elif opcion2=="2": elemen="managementIpAddress"
        elif opcion2=="3": elemen="macAddress"
        elif opcion2=="4": elemen="role"
        elif opcion2=="5": elemen="reachabilityStatus"  
        elif opcion2=="6": elemen="softwareVersion"
        else:
            break
    return

### INICIA LA TABLA QUE MOSTRAREMOS CON EL CONTADOR, para poder añadir 1 a 1 los valores a mostrar ###
def IniciaTablaElem(respHosts):
    hostList = []
    counter = 0
    for element in respHosts['response']:
        counter+=1
        host = [counter]
        hostList.append(host)
    tableHeader = ["Elemento"]

    DictMostrar=dict(one=hostList, two=tableHeader) 
    return DictMostrar

### FUNCION PARA MOSTRAR 1 A 1 LOS ELEMENTOS QUE LE INDIQUEMOS ###
def Mostrar(respHosts, DictMostrar, elem):
    #APLICANDO VALORES DEL SUBMENU
    print("\n Añadiendo variable para mostrar.......\n")
    hostListFinal = DictMostrar['one']

    # Recorre la respuesta json para obtener el elemento. Añade "" si no esta, y lo guarda en la lista
    hostNuevoElem= []
    mostrarelem = respHosts['response']
    for element in mostrarelem:
        if elem not in element:
            host = ""
        else:
            host=element[elem]
        hostNuevoElem.append(host)

    for i in range(len(hostListFinal)):
        hostListFinal[i].append(hostNuevoElem[i])

    tableHeader = DictMostrar['two']
    tableHeader.append(elem)

    print(tabulate(hostListFinal, tableHeader))
    DictMostrar=dict(one=hostListFinal, two=tableHeader)   
    return DictMostrar

def POST_Peticion(url, data):
    headers = {
        "Content-type" : "application/json",
        "X-Auth-Token": ticket
    }
    
    resp = requests.post(url, json.dumps(data), headers=headers, verify=False)

    resPost_json=resp.json()
    return resPost_json

### SUBMENU PARA ELEGIR DEL LISTADO DE DISPOSITIVOS DE RED LOS ELEMENTOS QUE QUEREMOS MOSTRAR EN UNA TABLA ###
def SubMenuLocaliz():
    while True:
        os.system("cls")
        print("\n*****************  SUB-MENU LOCALIZACION  *****************")
        print("***********************************************************\n")
        print("     1 - Mostrar Localizaciones")
        print("     2 - Crar nueva Localizacion")
        print(" ")
        print("    Pulsa cualquier otra tecla para Volver al menu PPAL")
        print(" -------------------------------------------------------------- ")
        #MostrarLocalizacion() 
        print(" > ")
        opcion2=input()
        os.system("cls")
        if opcion2=="1": MostrarLocalizacion()
        elif opcion2=="2": AñadirLocalizacion()
        else:
            break
    return

### MUESTRA EL LISTADO DE LAS LOCALIZACIONES EN FORMA DE TABLA ###
def MostrarLocalizacion():
    api_url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location"
    response_json=GET_Dispositivo(api_url)
    
    elemMostr= ['civicAddress','description', 'locationName','id']
    MostrarElementosIndicados(response_json, elemMostr)
    return response_json
 
### MUESTRA EN UNA TABLA LOS ELEMENTOS PASADOS EN UNA LISTA COMO ARGUMENTO ###
def MostrarElementosIndicados(respHosts, elem):

    tableHeader = ["Elemento"]
    for i in range(len(elem)):
        tableHeader.append(elem[i])
    
    print("                             *************     LISTADO DE LOCALIZACIONES  **************")
    print("                             ***********************************************************")
    print("\n ")

    hostListFinal =[]
    hostList = []
    counter = 0
    for resp in respHosts['response']: 
        counter+=1
        hostList=[counter]
        for lisElem in elem:
            if lisElem in resp:
                new = resp[lisElem]
            else:
                new=""
            hostList.append(new)
        hostListFinal.append(hostList)
                 
    print(tabulate(hostListFinal, tableHeader))
    input("\nPulsa Enter para continuar....")
    return


### SOLICITUD POST PARA CREAR UNA NUEVA LOCALIZACION ###
def AñadirLocalizacion():
    print("\n\n                           ************     AÑADIR NUEVA LOCALIZACION   *************")
    print("                           ***********************************************************")
    print("\n Introduce los siguientes datos.....  ")
    direc=input("\n   Nueva direccion: ")
    descrip=input("   Descripcion de la direccion: ")
    nombre=input("   Dale un nombre a la localizacion: ")

    api_url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location"

    datos={
        "civicAddress": direc,
        "description": descrip,
        "locationName": nombre,
    }

    respPos=POST_Peticion(api_url, datos)

    IdPeticion = respPos['response']['taskId']
    print("\nSe ha añadido correctamente, el ID de Petición es el siguiente: ", IdPeticion)
    input("\nPulsa Enter para continuar...")
    return IdPeticion

