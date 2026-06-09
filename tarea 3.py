import json

with open ("data.json","r") as file:
    config = json.load(file)

print ("Menu")


for i in range (config["intentos"]):
    if(i == config["intentos"]):
        print("Cantidad de intentos superada.")
        break
    user = input("ingrese usuario: ") 
    password = input("ingrese contrasena: ")
    if(user == config['user']):
        if(password == config['password']):
                print("Bienvenido al sistema.")
                ingresos = input("Ingrese su saldo:")
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
                                gasto ={ 
                                        'monto':input("monto"),
                                        'descripcion':input("descripcion: "),
                                        'operacion':input("operacion: ")
                                        }
                                with open ("registros.json","w") as file:
                                    json.dump(gasto,file)
                                   
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

