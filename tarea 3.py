print ("Menu")

user1 = "Edu"
password2 = "jesus1020"

for i in range (4):
    if(i == 3):
        print("Cantidad de intentos superada.")
        break
    user = input("ingrese usuario: ")
    password = input("ingrese contrasena: ")
    if(user == user1):
        if(password == password2 ):
                print("Bienvenido al sistema.")
                ingresos = input("Ingrese sus ingresos:")
                while True:
                    print("\n--- MENÚ DE OPCIONES ---")
                    print("1. Gestor de saldo")
                    print("2. Gestor de gastos")
                    print("3. Salir")
        
                    opcion = input("Seleccione una opción (1-3): ")

                    if opcion == "1":
                        while True:
                            print("Su saldo es: " + str(ingresos))
                            print("desea agregar ingresos? (s/n)")
                            respuesta = input()
                            if respuesta == "s":
                                nuevos_ingresos = input("Ingrese los nuevos ingresos: ")
                                ingresos = int(ingresos) + int(nuevos_ingresos)
                                print("Ingresos agregados. Su nuevo saldo es: " + str(ingresos))
                            else:
                                print("No se han agregado nuevos ingresos.") 
                                break   
                    elif opcion == "2":
                        gastos = input("Cuantos gastos has hecho?")

                        acumulador = 0

                        for i in range (int(gastos)):
                            gasto = input ("ingrese el gasto "+str(i+1)+":")
                            acumulador = acumulador + int(gasto)
                        print("El total de gastos es: "+str(acumulador)," y su saldo restante es: "+str(int(ingresos)-acumulador))
                    elif opcion == "3":
                        print("Saliendo del programa...")
                        break # Rompe el bucle while y termina
                    else:
                        print("Opción no válida. Intente de nuevo.")
            
        else:
            print ("contraseña incorrecta.")
    else:
        print("usuario incorrecto.")

