disponible =(int(input("Bienvenido, Cual es tu saldo? ")))
gastos = input("Cuantos gastos has hecho?")

acumulador = 0

for i in range (int(gastos)):
    gasto = input ("ingrese el gasto "+str(i+1)+":")
    acumulador = acumulador + int(gasto)

print ("hoy has gastado: " + str(acumulador),"y ten quedan: " + str(disponible-int(acumulador)))