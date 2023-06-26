import numpy as np
tipo = []
patente = []
marca = []
precio = []
multa_monto = []
multa_fecha = []
fecha_registro = []
nombre_dueño = []
poto = 0
c=0
y=0
def grabar():
    validadorpatente = True
    validadormarca = True
    validadorprecio = True

    tipo.append(str(input("Ingrese el Tipo de Vehiculo: ")))
    while validadorpatente==True:
            patente.append(input("Ingrese la PATENTE del Vehiculo ( Debe contener 6 digitos)"))
            if len(patente[y])==6:
                validadorpatente=False
            else:
                print("Vuelva a ingresar la PATENTE")
    while validadormarca == True:
            marca.append(input("Ingrese la Marca del Vehiculo: "))
            if len(marca [y])>=2 and len(marca[y])<= 15:
                validadormarca = False
            else:
                print("Vuelva a ingresar la MARCA")
    while validadorprecio == True:
            precio.append(int(input("Ingrese el Precio del Vehiculo: ")))
            if precio[y] > 4999999:
                validadorprecio = False
            else:
                print("Vuelva a ingresar el PRECIO")
            multa_monto.append(int(input("Ingrese el Monto de la Multa del Vehiculo / Si no tiene multas ingrese 0: ")))
            multa_fecha.append(input("Ingrese la Fecha de la Multa del Vehiculo / Si no tiene multas ingrese 0: "))
            fecha_registro.append(int(input("Ingrese la Fecha de Registro del Vehiculo: ")))
            nombre_dueño.append(str(input("Ingrese el Nombre del Dueño del Vehiculo: ")))
def buscar():
        buscar = input("Ingrese la PATENTE del Vehiculo a buscar: ")
        for i in patente:
            if i == buscar:
                c = 0
                print("El tipo de vehiculo es: ",tipo[c])
                print("La patente del vehiculo es: ",patente[c])
                print("La marca del vehiculo es: ",marca[c])
                print("El precio del vehiculo es: ",precio[c])
                if multa_monto[c]==0 and multa_fecha[c]==0:
                    print("El vehiculo no presenta Multas")
                else:
                    print("El valor de la multa es: ", multa_monto[c])
                    print("La fecha de la multa es: ", multa_fecha[c])
                print("La fecha de registro del vehiculo es: ",fecha_registro[c])
                print("El nombre del dueño del vehiculo es: ",nombre_dueño[c])
                c+=1
            else:
                print("PATENTE no encontrada/registrada")
def menu():
        print("------MENU------")
        print("Opcion 1. Grabar un Vehiculo")
        print("Opcion 2. Buscar un Vehiculo")
        print("Opcion 3. Imprimir Certificados")
        print("Opcion 4. Salir ")
        print("----------------")
def imprimir_certificado():
  certificado = int(input("Escoja el Certificado a Imprimir: "))
  if certificado == 1:
       certificado = "Emision de contaminantes"
  elif certificado == 2:
       certificado = "Anotaciones Vigentes"
  elif certificado == 3:
       certificado = "Multas"
  for i in range(len(patente)):
      valor = np.random.randint(1500, 3500)
      print("Certificado: ", certificado)
      print("Patente del Vehiculo: ", patente[c])
      print("Nombre Dueño del Vehiculo: ", nombre_dueño[c])
      print("Valor Certificado: ", valor)
while poto == 0:
    menu()
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion == 1:
         grabar()    
    if opcion == 2:
        buscar()
    if opcion == 3:
         print("------CERTIFICADOS------")
         print("1. Emision de Contaminantes")
         print("2. Anotaciones Vigentes")
         print("3. Multas")
         print("------------------------")
         imprimir_certificado()
    if opcion == 4:
        poto = 1
        print("Hasta luego\n created by Vicente Tramon\n v.01")