import json
import requests,json

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
                    print("4. Ventana de divisas")
                    print("5. Calculadora de divisas")
                    print("6. Salir")
                    opcion = input("Seleccione una opción (1-6): ")

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
                                movimiento = {
                                'monto':nuevos_ingresos,
                                'descripcion':input("Descripcion: "),
                                'operacion':("ingreso.")
                                }
                                with open ("registros.json","r") as file:
                                        lista=json.load(file)
                                        if not isinstance(lista, list):
                                            lista = []
                                lista.append(movimiento)
                                with open ("registros.json","w") as file:
                                    json.dump(lista,file)
                                    print("Ingreso añadido.") 
                                print("Ingresos agregados, Su nuevo saldo es: "+ str(config["saldo"]))
                            else:
                                print("No se han agregado nuevos ingresos.") 
                                break
                                
                    elif opcion == "2":
                        gasto = input ("Ingrese el gasto: ")
                        if float(gasto) > float(config["saldo"]):
                            print("No tiene suficiente saldo para realizar este gasto.")
                            break

                        elif float(gasto) <= float(config["saldo"]):
                            config["saldo"] = float(config["saldo"]) - float(gasto)
                            with open ("data.json","w") as file:
                                json.dump(config,file)
                            print("Su gasto es: "+str(gasto)+" y su saldo restante es: "+str(config["saldo"]))
                            movimiento = {
                                'monto':gasto,
                                'descripcion':input("Descripcion: "),
                                'operacion':("gasto: ")
                                }
                            with open ("registros.json","r") as file:
                                    lista=json.load(file)
                                    if not isinstance(lista, list):
                                        lista = []
                            lista.append(movimiento)
                            with open ("registros.json","w") as file:
                                json.dump(lista,file)
                                print("Gasto añadido")
                        else:
                            print("Ocurrió un error al procesar el gasto.")
                            break

                    elif opcion == "3":
                        print("Historial de movientos")
                        print(f"Saldo actual: {config['saldo']}")
                        print("Cargando...")
                        print("Movimientos:")
                        with open ("registros.json","r") as file:
                            movimiento = json.load(file)
                            for i, movimiento in enumerate(movimiento, start=1):
                                print (f"Movimiento #{i}:")
                                print (f" Movimiento de: {movimiento['monto']}bs.")
                                print (f" Descripcion: {movimiento['descripcion']}")
                                print (f" Operacion: {movimiento['operacion']}")
                    
                    elif opcion == "4":

                        print("Ventana de Divisas")
                        print("1. Dolar")
                        print("2. Euro")

                        opcion_divisa = input("Seleccione una opción (1-3): ")
                        if opcion_divisa == "1":
                            response = requests.get("https://ve.dolarapi.com/v1/dolares/oficial")
                            dolar_data = response.json()
                            dolar = float(config["saldo"]) / (dolar_data["promedio"])
                            print(f"Su saldo en dolares es: {dolar}")

                        elif opcion_divisa == "2":
                            response = requests.get("https://ve.dolarapi.com/v1/euros/oficial")
                            euro_data = response.json()
                            euro = float(config["saldo"]) / (euro_data["promedio"])
                            print(f"Su saldo en euros es: {euro}")

                        else:
                            print("Opción no válida. Intente de nuevo.")
                    
                    elif opcion == "5":
                        print("Calculadora de divisas")
                        print("1. Dolar a Bolivares")
                        print("2. Euro a Bolivares")

                        opcion_calculadora = input("Seleccione una opción (1-2): ")
                        if opcion_calculadora == "1":
                            cantidad_dolar = float(input("Ingrese la cantidad en dólares: "))
                            response = requests.get("https://ve.dolarapi.com/v1/dolares/oficial")
                            dolar_data = response.json()
                            bolivares = cantidad_dolar * (dolar_data["promedio"])
                            print(f"{cantidad_dolar} dólares equivalen a {bolivares} bolívares.")

                        elif opcion_calculadora == "2":
                            cantidad_euro = float(input("Ingrese la cantidad en euros: "))
                            response = requests.get("https://ve.dolarapi.com/v1/euros/oficial")
                            euro_data = response.json()
                            bolivares = cantidad_euro * (euro_data["promedio"])
                            print(f"{cantidad_euro} euros equivalen a {bolivares} bolívares.")

                        else:
                            print("Opción no válida. Intente de nuevo.")

                    elif opcion == "6":
                        print("Saliendo del programa...")
                        break 
                    else:
                        print("Opción no válida. Intente de nuevo.")
            
        else:
            print ("contraseña incorrecta.")
    else:
        print("usuario incorrecto.")

