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