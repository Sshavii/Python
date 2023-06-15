import numpy as np

def calcular_iva(TotalCompra):
    iva = TotalCompra*0.19
    print("El IVA es de",iva)
def descuento (TotalCompra):
    valor_descuento = TotalCompra *3/100
    print("Su descuento es de ",valor_descuento)
def calcular_imc(peso,altura):
    resultado_imc = round((peso / altura**2),1)
    return resultado_imc
def estado_imc(imc):
    if imc<18.5:
        print("ESTADO - BAJO PESO")
    elif imc>=18.5 and imc<=24.9:
        print("ESTADO - ADECUADO")
    elif imc>=25.0 and imc>29.9:
        print("ESTADO - SOBREPESO")
    elif imc>=30.0 and imc<=34.9:
        print("ESTADO - OBESIDAD GRADO 1")
    elif imc>= 35.0 and imc>=39.9:
        print("ESTADO - OBESIDAD GRADO 2")
    elif imc<40:
        print("ESTADO - OBESIDAD GRADO 3")
def menu():
    print("----------MENU---------")
    print("1. Calcular IVA")
    print("2. Calcular Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
poto=1
while poto == 1:
    menu()
    opcion = int(input("Ingrese la OPCION que desea: "))
    if opcion == 1:
        TotalCompra = int(input("Ingrese el valor de su compra: "))
        calcular_iva(TotalCompra)
    elif opcion == 2:
        TotalCompra = int(input("Ingrese el valor total: "))
        descuento(TotalCompra)
    elif opcion == 3:
        peso = int(input("Ingrese su peso: "))
        altura = float(input("Ingrese su altura: "))
        imc = calcular_imc(peso,altura)
        print("Su IMC es de: ",imc)
        estado_imc(imc)
    elif opcion == 4:
        print("-----ADIOS-----")
        poto = 0
