


import random

class auto:
    def __init__(self, patente, marca, tipo, precio, multas, fech_registro, dueño):
        self.patente = patente
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.multas = multas
        self.fech_registro = fech_registro
        self.dueño = dueño
    



def ingreso_vei(autos):
    patente = input("patente: ")
    marca = input("marca: ")
    tipo = input("ingrese tipo de vehiculo: ")

    if not valida_patente(patente):
        print("Esta patente es incorrecta, ingrese una nuevamente " )
        return
    
    marca = input("marca:")

    precio = float(input("ingrese un precio mayor a $5.000.000:"))
    if precio   <= 5000000:
        print("El precio que ha ingresado es igual o meno a 5.000.000, vuelva a ingresar un precio: ")
        return
    
    monto_multas = float(input("ingrese monto de multas: "))

    fecha_multas = input("ingrese fecha de sus multas: ")

    fech_registro = input("ingrese año de su auto: ")

    dueño = input("ingrese nombre y apellido del dueño: ")

    auto = vehiculo(patente, marca, precio, tipo, (monto_multas, fecha_multas) ,fech_registro, dueño)
    autos[patente] = auto 
    print( " auto registrado correctamente. ")

def buscar_vehiculo(autos):
    patente = input("ingrese la patente del auto qque desea consultar: ")
    
    if patente in autos:
        auto = autos[patente]
        print("estos son los datos del auto con patente {auto.patente}:")
        print(f"patente: {auto.patente}")
        print(f"marca: {auto.marca}")
        print(f"precio: {auto.precio}")
        print(f"tipo: {auto.tipo}")
        print(f"multas {auto.multas}")
        print(f"año auto: {auto.fech_registro}")
        print(f"nombre del dueño: {auto.dueño}")
    else:
        print("la patente ingresada no registra un auto ")

def Mostrar_certificados(autos):
    for patente , auto in autos():


def menu():
    autos = {}
    while True:
        print("\nmenu inicial:")
        print("1.registrar vehiculo")
        print("2.consultar vehiculo")
        print("3.consultar certificado del vehiculo")
        print("4.salir.")


        opc = input("ingrese la opcion que desea realizar: ")
        if opc == "1":
            ingreso_vei(autos) 
        elif opc == "2":
            buscar_vehiculo(autos)
        elif opc == "3":
            Mostrar_certificados
        elif opc == "4":
            print("eligio salir del menu, adios")
        else:
            print("ingrese una opcion valida")










