import json
import requests,json

def leer():
    with open ("registros.json","r") as file:
        x = json.load(file)
        return x    

      

with open ("data.json","r") as file:
    config = json.load(file)

print("Menu")
print("Bienvenido")
print("Inicie sesión")
print("Tienes: 3 intentos para ingresar al sistema.")
for i in range (config["intentos"]):

    if(i == 3):
        print("Cantidad de intentos superada.")
        break
    user = input("Ingrese usuario: ") 
    password = input("Ingrese contrasena: ")
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
                    print("6. Estadisticas financieras")
                    print("7. Analisis rapido")
                    print("8. Análisis total")
                    print("9. Zona de control")
                    print("10. Salir")
                    opcion = input("Seleccione una opción (1-10): ")

                    if opcion == "1":
                        while True:
                            print("Su saldo es: "+ str(config["saldo"]),"Bs")
                            print("Desea agregar ingresos? (s/n)")
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
                                print("Ingresos agregados, su nuevo saldo es: "+ str(config["saldo"]),"Bs")
                            else:
                                print("No se han agregado nuevos ingresos.") 
                                break

                    elif opcion == "2":
                        while True:          
                            gasto = input ("Ingrese el gasto: ")
                            if float(gasto) > float(config["saldo"]):
                                print("No tiene suficiente saldo para realizar este gasto.")
                                break

                            elif float(gasto) <= float(config["saldo"]):
                                config["saldo"] = float(config["saldo"]) - float(gasto)
                                with open ("data.json","w") as file:
                                    json.dump(config,file)
                                print("Su gasto es: "+str(gasto),"Bs.")
                                print("Su saldo restante es: "+str(config["saldo"]),"Bs")
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
                                    break
                            else:
                                print("Ocurrió un error al procesar el gasto.")
                                break

                    elif opcion == "3":
                        print("Historial de movientos")
                        print(f"Saldo actual: {config['saldo']}Bs")
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

                        opcion_divisa = input("Seleccione una opción (1-2): ")
                        if opcion_divisa == "1":
                            response = requests.get("https://ve.dolarapi.com/v1/dolares/oficial")
                            dolar_data = response.json()
                            dolar = float(config["saldo"]) / (dolar_data["promedio"])
                            print(f"Su saldo en dolares es: {dolar}$")
                            continue
                        elif opcion_divisa == "2":
                            response = requests.get("https://ve.dolarapi.com/v1/euros/oficial")
                            euro_data = response.json()
                            euro = float(config["saldo"]) / (euro_data["promedio"])
                            print(f"Su saldo en euros es: {euro}€")
                            continue
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
                            print("Valor del dolar: " + str(dolar_data["promedio"]))
                        elif opcion_calculadora == "2":
                            cantidad_euro = float(input("Ingrese la cantidad en euros: "))
                            response = requests.get("https://ve.dolarapi.com/v1/euros/oficial")
                            euro_data = response.json()
                            bolivares = cantidad_euro * (euro_data["promedio"])
                            print(f"{cantidad_euro} euros equivalen a {bolivares} bolívares.")
                            print("Valor del euro: " + str(euro_data["promedio"]))
                        else:
                            print("Opción no válida. Intente de nuevo.")

                    elif opcion == "6":
                        print("Estadisticas financieras")
                        with open ("registros.json","r") as file:
                            registros = json.load(file)
                        if not registros:
                            print("No hay registros disponibles.")  
                        else:
                            total_ingresos = 0.0 
                            total_gastos = 0.0  
                            cantidad_ingresos = 0
                            cantidad_gastos = 0 
                        for registros in registros:
                            monto = float(registros['monto'])
                            tipo = registros['operacion']
                            if tipo == "ingreso.":
                                    total_ingresos += monto
                                    cantidad_ingresos += 1
                            elif tipo == "gasto: ":
                                total_gastos += monto
                                cantidad_gastos += 1
                                balance = total_ingresos - total_gastos
                        print(f"Total de ingresos: {total_ingresos} Bs. {cantidad_ingresos} ingresos.")
                        print(f"Total de gastos: {total_gastos} Bs. {cantidad_gastos} gastos.")
                        print(f"Balance actual: {balance} Bs.")

                    elif opcion == "7":
                        print("Analisis rapido")
                        with open ("registros.json","r") as file:
                            registros = json.load(file)    
                            total_ingresos = 0.0 
                            total_gastos = 0.0  
                            cantidad_ingresos = 0
                            cantidad_gastos = 0 
                        for registros in registros:
                            monto = float(registros['monto'])
                            tipo = registros['operacion']
                            if tipo == "ingreso.":
                                    total_ingresos += monto
                                    cantidad_ingresos += 1
                            elif tipo == "gasto: ":
                                    total_gastos += monto
                                    cantidad_gastos += 1
                                    balance = total_ingresos - total_gastos
                        if balance < 0:
                                        print("¡Cuidado! Estás gastando más de lo que ingresas.")
                        elif balance == 0:
                                        print("Estás equilibrado, pero ten cuidado con tus gastos.")
                        else:
                                        print("¡Buen trabajo! Estás gastando menos de lo que ingresas.")

                    elif opcion == "8":
                        print("Análisis total")
                        with open ("registros.json","r") as file:
                            registros = json.load(file)    
                            total_ingresos = 0.0 
                            total_gastos = 0.0  
                            cantidad_ingresos = 0
                            cantidad_gastos = 0 
                        for registros in registros:
                            monto = float(registros['monto'])
                            tipo = registros['operacion']
                            if tipo == "ingreso.":
                                    total_ingresos += monto
                                    cantidad_ingresos += 1
                            elif tipo == "gasto: ":
                                    total_gastos += monto
                                    cantidad_gastos += 1
                                    balance = total_ingresos - total_gastos
                            porcentaje_gastos = (total_gastos / total_ingresos) * 100 if total_ingresos > 0 else 0
                        print (f"Has gastado el {porcentaje_gastos:.1f}% de tus ingresos totales.")

                    elif opcion == "9":
                        print("ZONA DE CONTROL CRITICO")
                        confirmar = input("¿Estás seguro de que deseas acceder a esta zona? (s/n): ")
                        if confirmar == "s":
                            final = input("¡Alerta! Has accedido a la zona de control crítico. Seguro de eliminar todos los datos? (s/n): ")
                            if final == "s":
                                config["saldo"] = 0.0
                                with open ("data.json","w") as file:
                                    json.dump(config,file, indent=4)
                                with open ("registros.json","w") as file:    
                                    json.dump([],file, indent=4)
                                print("¡Alerta! Has accedido a la zona de control crítico. Tu saldo ha sido restablecido a 0 y tus registros han sido eliminados.")
                                break
                            else:
                                print("Acceso a la zona de control crítico cancelado de forma segura.")
                        else:
                            print("Acceso a la zona de control crítico cancelado de forma segura.")    
                            break

                    elif opcion == "10":
                        print("Saliendo del programa...")
                        break 

                    else:
                        print("Opción no válida. Intente de nuevo.")

        else:
            print ("Contraseña incorrecta.")
    else:
        print("Usuario incorrecto.")