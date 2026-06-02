print ("Menu")

user1 = "Edu"
password2 = "jesus1020"

for i in range (3):
    if(i == 2):
        print("Cantidad de intentos superada.")
        break
    user = input("ingrese usuario: ")
    password = input("ingrese contrasena: ")
    if(user == user1):
        if(password == password2 ):
            print ("Inciaste.")
            disponible =(int(input("Bienvenido, Cual es tu saldo? ")))
            gastos = input("Cuantos gastos has hecho?")

            acumulador = 0

            for i in range (int(gastos)):
                gasto = input ("ingrese el gasto "+str(i+1)+":")
                acumulador = acumulador + int(gasto)

            print ("hoy has gastado: " + str(acumulador),"y ten quedan: " + str(disponible-int(acumulador)))
            break
        else:
            print ("contraseña incorrecta.")
    else:
        print("usuario incorrecto.")



