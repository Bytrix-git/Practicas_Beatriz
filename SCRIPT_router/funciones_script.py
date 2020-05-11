#!/usr/bin/env python3
from ncclient import manager
import xml.dom.minidom
from pprint import pprint
from os import system
import xmltodict
from tabulate import *
import time

global conexion

# Creamos un objeto con la sesion NETCONF: 
conexion = manager.connect(
         host="192.168.56.101",
         port=830,
         username="cisco",
         password="cisco123!",
         hostkey_verify=False
         )

def TablaInterfaces():
    netconf_filter = """
    <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    netconf_reply = conexion.get(filter = netconf_filter)
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

   # INICIALIZO LA TABLA CON EL ELEMENTO y los datos NOMBRE y DIR IP
    respIfces_N1 = netconf_reply_dict["rpc-reply"]["data"]["interfaces"]["interface"]
    respIfces_N0 = netconf_reply_dict["rpc-reply"]["data"]["interfaces"]
    TablaElem = []
    contador = 1

    # PARA EL CASO EN QUE NO TENGA NINGUNA CONFIGURADA
    LisRouter0=[]
    for i in respIfces_N0.values():
        LisRouter0.append(i)

    if 'name' in LisRouter0[1]:
        nombre = LisRouter0[1]['name']
        ip = "IP sin configurar"
        device = [                                  # Crea la lista que será mostrada
                    contador,
                    nombre,
                    ip,
                    ]
        TablaElem.append(device)                    # Añade esta lista por cada interfaz 
        contador += 1
    else:
        for networkElement in respIfces_N1:
            nombre = networkElement['name']
            if "address" not in networkElement["ipv4"]:
                ip = "sin ip"
            else:  
                ip = networkElement["ipv4"]["address"]["ip"]
            device = [
                    contador,
                    nombre,
                    ip,
                    ]
            TablaElem.append(device)
            contador += 1

    tableHeader = ["Elemento", "NombreIfz", "Direccion IP"]         #[[1, 'Loopback99', '99.99.99.99'], [2, 'Loopback100', '100.100.100.100']]

    ## AÑADIMOS LA INFORMACION DE DIRECCION MAC
    netconf_filter = """
    <filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    netconf_reply = conexion.get(filter = netconf_filter)
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

    respIfces_N1 = netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]
    respIfces_N0 = netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]

    LisRouter0=[]
    for i in respIfces_N0.values():
        LisRouter0.append(i)

    NuevoElem = []
    #### PRIMERA COMPROBACION SI EL ROUTER ESTA VACIO CON SOLO 1 IFZ
    if 'phys-address' in LisRouter0[1]:
        mac=LisRouter0[1]['phys-address']
        NuevoElem.append(mac)
        for i in range(len(TablaElem)):
            TablaElem[i].append(NuevoElem[i])
    else:
        for element in respIfces_N1:
            if "phys-address" not in element:
                mac = ""
                continue
            else:
                mac=element["phys-address"]
            NuevoElem.append(mac)
        for i in range(len(TablaElem)):
            TablaElem[i].append(NuevoElem[i])

    tableHeader.append("Direccion MAC")
    print(tabulate(TablaElem, tableHeader))
    return

def NuevaIfzLoopback():
    TablaInterfaces()
    print("\nIntroduce los nuevos datos del interfaz: ")
    ip_nueva=input("Direccion IP: ")
    nombre=input("Nombre: ")
    #comentario=input("Descripcion: ")
    mascara=input("Mascara de subred: ")

    netconf_data = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <Loopback>
        <name>"""+nombre+"""</name>
        <description>Interfaz de loopback creada con NETCONF</description>
        <ip>
        <address>
        <primary>
        <address>"""+ip_nueva+"""</address>
        <mask>"""+mascara+"""</mask>
        </primary>
        </address>
        </ip>
    </Loopback>
    </interface>
    </native>
    </config>
    """
    # Incluimos la nueva info 
    try:
        netconf_reply = conexion.edit_config(target="running", config=netconf_data)
    except:
        print("\nERROR AL CREAR LA NUEVA INTERFAZ: Comprueba que has introducido los datos correctamente")
        print(" y que no estás creando la interfaz con el mismo nombre que otra ya existente")
        pass
    else:
        print("\n Interfaz creada correctamente")
        TablaInterfaces()

    input("\nPulsa Enter para continuar")
    return


def BorrarIfzLoopback(): 
    TablaInterfaces()
    print("\nIntroduce los datos del interfaz a borrar: ")
    nombre=input("Nombre: ")

    netconf_data = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <Loopback operation="delete">
        <name>"""+nombre+"""</name>
    </Loopback>
    </interface>
    </native>
    </config>
    """

    try:
        netconf_reply = conexion.edit_config(target="running", config=netconf_data,default_operation=None,)
    except:
        print("\nERROR AL BORRAR LA INTERFAZ: Comprueba que has introducido los datos correctamente")
        print("******  Ten en cuenta que sólo se borrarán aquellas que estén   ******")
        print("****** en la running-config y que NO sean Interfaces Físicas!!! ******")
        pass                      
    else:
        print("\n Interfaz borrada correctamente")
        print("\n")
        TablaInterfaces()
    input("\nPulsa Enter para continuar")
    return

def peticionCapab():
    router_capab= []
    contador=0
    for c in conexion.server_capabilities:
        if c.startswith('http://cisco.com/'):
            capab=[contador, c]
            router_capab.append(capab)
            contador+=1

    print("\nEstas son algunas de las CAPABILITIES COMPATIBLES con nuestro dispositivo: ")
    for i in range(15):
        time.sleep(0.2)
        print("      ",router_capab[i][1])
    print("      Y muchas más...\n")
    
    print("Y aquí tienes 2 ejemplos para mostrarte la informacion configurada que pueden modificar estos Modulos Yang")
    print("1 - Cifrado")
    print("2 - Protocolo Multilik PPP")
    print("Pulsa cualquier otra tecla para continuar")

    while True:
        capamostrar=input("\n")
        if capamostrar=="1":
            system("cls")
            print("\n\n ***** MOSTRANDO CAPABILITY...... http://cisco.com/ns/yang/Cisco-IOS-XE-crypto ***** \n\n")
            netconf_filter = """
            <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <crypto>
                <pki xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto">
                </pki>
            </crypto>
            </native>
            </filter>
            """
            netconf_reply = conexion.get( filter = netconf_filter)
            print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )
            print("\n ***** Selecciona 2 si quieres ver el otro ejemplo o Enter para volver al menu principal ***** ", end=" ")
        
        elif capamostrar=="2":
            system("cls")
            print("\n\n ***** MOSTRANDO CAPABILITY...... http://cisco.com/ns/yang/Cisco-IOS-XE-ppp *****\n\n")
            netconf_filter = """
            <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <multilink>
                        <bundle-name xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ppp">
                        </bundle-name>
                </multilink>
            </native>
            </filter>
            """
            netconf_reply = conexion.get( filter = netconf_filter)
            print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )
            print("\n ***** Selecciona 1 si quieres ver el otro ejemplo o Enter para volver al menu principal *****", end=" ")
        else:
            break
    return

def TablaRouting():
    netconf_filter = """
    <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    netconf_reply = conexion.get(filter = netconf_filter)
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

   # INICIALIZO LA TABLA CON EL ELEMENTO y los datos NOMBRE y DIR IP
    respIfces_N1 = netconf_reply_dict["rpc-reply"]["data"]["interfaces"]["interface"]
    respIfces_N0 = netconf_reply_dict["rpc-reply"]["data"]["interfaces"]

    TablaElem = []
    contador = 1

    LisRouter0=[]
    for i in respIfces_N0.values():
        LisRouter0.append(i)
    
    if 'name' in LisRouter0[1]:                 # CON EL ROUTER SIN INICIALIZAR
        nombre = LisRouter0[1]['name']
        ip = "IP sin configurar"
        neighbor = "not connected"
        device = [ 
                    contador,
                    ip,
                    nombre,
                    neighbor,
                    ]
        TablaElem.append(device) 
        contador += 1

    else:
        for networkElement in respIfces_N1:
            nombre = networkElement['name']
            if "address" not in networkElement["ipv4"]:
                ip = "no ip"
                if "neighbor" not in networkElement["ipv4"]:
                    neighbor = "not connected"
                else:
                    neighbor=networkElement["ipv4"]["neighbor"]["ip"]
            else:  
                ip = networkElement["ipv4"]["address"]["ip"]
                if "neighbor" not in networkElement["ipv4"]:
                    neighbor = "not connected"
                else:
                    neighbor=networkElement["ipv4"]["neighbor"]["ip"]
            device = [   
                    contador,
                    ip,
                    nombre,
                    neighbor,
                    ]
            TablaElem.append(device)    
            contador += 1

    tableHeader = ["Elemento", "Direccion IP", "Ifz Salida", "Dispositivo Conectado"]
    print(tabulate(TablaElem, tableHeader))  
    input("\nPulsa Enter para continuar")
    return


    