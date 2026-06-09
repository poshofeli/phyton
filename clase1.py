print("Hola,bienvenido.")
nombre = input("Cual es tu nombre?")
edad = int(input("Cual es tu edad?"))
if(edad >=18):
    disponible =(int(input("Bienvenido, "+nombre+" Cual es tu saldo? ")))
    gasto = input("Cual ha sido tu primer gasto hoy? ")
    gasto2 = input("Cual ha sido tu segundo gasto hoy? ")
    gasto3 = input("Cual ha sido tu tercer gasto hoy? ")
    gastototal =float(gasto) + float(gasto2) + float(gasto3)
    if(disponible>gastototal):
        actual = disponible-gastototal
        print("saldo actual:"+actual)  
    else:   
        print("saldo insuficiente")  

else:
    print("acceso denegado, inicie sesion nuevamente")
nombre = str(input("Ingrese nombre:"))
print("Bienvenido "+nombre)

p1 = float(input("Precio del producto:"))
p2 = float(input("Precio del producto:"))
p3 = float(input("Precio del producto:"))

total = p1+p2+p3
if(total >100):
    descuento = total*15/100
elif(total >=70 and total <=100):
    descuento = total*10/100
else:
    print(float("total"))
print("total:",int(total),"\ndescuento de:",descuento,"\nTotal a pagar "+str(total-descuento))   