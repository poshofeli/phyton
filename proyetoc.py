import json

with open ("data.json","r") as file:
    config = json.load(file)

print("Menu")
print("Bienvenido")
for i in range (config["intentos"]):

    if(i == 3):
        print("Cantidad de intentos superada.")
        break
    user = input("ingrese usuario: ") 
    password = input("ingrese contrasena: ")
    if(user == config['user']):
        if(password == config['password']):
                print("Bienvenido al sistema.")

                while True:
                    print("\n--- MENÚ DE OPCIONES ---")
                    print("1. Gestor de saldo")
                    print("2. Gestor de gastos")
                    print("3. Historial de movientos")
                    print("4. Divisas")
                    print("5. Salir")
                  
                    opcion = input("Seleccione una opción (1-3): ")

                    if opcion == "1":
                        while True:
                            print("Su saldo es: "+ str(config["saldo"]))
                            print("desea agregar ingresos? (s/n)")
                            respuesta = input()
                            if respuesta == "s":
                                nuevos_ingresos = input("Ingrese los nuevos ingresos: ")
                                config["saldo"] = float(config["saldo"]) + float(nuevos_ingresos)
                                with open ("data.json","w") as file:
                                     json.dump(config,file)
                                gasto ={ 
                                        'monto':(nuevos_ingresos),
                                        'descripcion':input("descripcion: "),
                                        'operacion':("operacion: Ingreso")
                                        }
                                with open ("registros.json","w") as file:
                                    json.dump(gasto,file)
                                    print("Ingreso añadido")
                                   
                                print("Ingresos agregados, Su nuevo saldo es: "+ str(config["saldo"]))
                            else:
                                print("No se han agregado nuevos ingresos.") 
                                break   
                    elif opcion == "2":

                        gasto = input (float("Ingrese el gasto: "))
                        config["saldo"] = float(config["saldo"]) - float(gasto)
                        with open ("data.json","w") as file:
                                json.dump(config,file)
                        print(f"El total de gastos es: "+float(gasto)," y su saldo restante es: "+float(config["saldo"]))
                        gasto ={ 
                                        'monto':input("monto"),
                                        'descripcion':input("Descripcion: "),
                                        'operacion':input("Operacion: gasto ")
                                        }
                        with open ("registros.json","w") as file:
                                    json.dump(gasto,file)
                                    print("Gasto añadido")
                    elif opcion == "3":
                        print("Historias de movientos")
                        with open ("registros.json"),"r" as file:
                            json.dump(gasto,file)
                            #print("Gasto de: [("monto")]\n Descripcion: [("descripcion")]\nOperacion: [()"ingreso")])
                    
                    elif opcion == "4":
                        pass
                                   
                    elif opcion == "5":
                        print("Saliendo del programa...")
                        break 
                    else:
                        print("Opción no válida. Intente de nuevo.")
            
        else:
            print ("contraseña incorrecta.")
    else:
        print("usuario incorrecto.")

