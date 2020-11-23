import csv
import os.path



# ------- Funcion crea archivo con csv.DictWriter
def creaArchivo(nombre, lista):
    cabecera = ["Legajo", "Apellido" , "Nombre" , "Total Vacaciones"]

    with open(nombre, "w") as newF:
        newFile = csv.DictWriter(newF,fieldnames=cabecera)

        newFile.writeheader()
        newFile.writerows(lista)


    print(f"\t{nombre}.csv ha sido creado con exito. ")
    return

# ------- Funcion edita archivo con csv.DictWriter sin eliminar lo que hay previamente.
def editarArchivo(nombre, lista):
    cabecera = ["Legajo", "Apellido" , "Nombre" , "Total Vacaciones"] # Sigue siendo necesario el fieldnames, asi que se deja cabeceras

    with open(nombre, "a") as newF:
        newFile = csv.DictWriter(newF,fieldnames=cabecera)

        newFile.writerows(lista) # Solo agrega las lineas nuevas.


    print(f"\t{nombre}.csv ha sido EDITADO con exito. ")
    return

# ------- Funcion borra y sobreescribe archivo con csv.DictWriter eliminando y reemplazando lo que hay previamente.


def sobreescribeArchivo(nombre, lista):
    cabecera = ["Legajo", "Apellido" , "Nombre" , "Total Vacaciones"]

    with open(nombre, "w") as newF:
        newFile = csv.DictWriter(newF,fieldnames=cabecera)

        newFile.writeheader() # Escribe cabeceras
        newFile.writerows(lista) # Escribe lineas


    print(f"\t{nombre}.csv ha sido SOBREESCRITO con exito. ")
    return

# ------- Funcion toma los datos para crear lista de diccionarios y valida los datos enteros antes de llamar a funcion que crea el archivo

def cargarVacaciones():
    nombreNew = input("\t\nNombre para el archivo .csv: ")
    nombreNew = f"{nombreNew}.csv"  # Le damos el formato .csv al nombre del archivo
    cabecera = ["Legajo", "Apellido" , "Nombre" , "Total Vacaciones"] # Cabeceras usadas para iterar sobre los input de usuario
    listaCarga =[] # Lista para guardar los diccionarios clave valor generados por cada vuelta de bucle for.
    cargar = "" # Variable de control

    archivoExistente = os.path.isfile(nombreNew) # regresa valor booleano si existe el archivo con nombreNew

    if archivoExistente == True: # Menu de acciones en caso de existir archivo
        print("\t\nEl archivo ya existe..")
        menuCarga = input("\t\n1: Agregar legajo. \n2: Sobreescribirlo. \n3: Volver a Menu principal \n: ")

        if int(menuCarga)== 1:
            print("Opcion 1:  Agregar legajo. ")
            while cargar != "n":
                diccCarga = {"Total Vacaciones":0}
                for i in cabecera:
                    diccCarga[i] = (input(f"\n\tIngrese {i}: "))
                    try:
                        int(diccCarga["Legajo"])
                        int(diccCarga["Total Vacaciones"])


                    except:
                        print("\n\tLegajo y vacaciones debe ser un numero.")
                        return
                listaCarga.append(diccCarga)
                cargar = input(f"\n\tDesea cargar otro registro? s/n: ")

            return editarArchivo(nombreNew, listaCarga)



        if int(menuCarga)== 2:
            print("Opcion 2: sobreescribir. ")
            while cargar != "n":
                diccCarga = {"Total Vacaciones":0}
                for i in cabecera:
                    diccCarga[i] = (input(f"\n\tIngrese {i}: "))
                    try:
                        int(diccCarga["Legajo"])
                        int(diccCarga["Total Vacaciones"])


                    except:
                        print("\n\tLegajo y vacaciones debe ser un numero.")
                        return
                listaCarga.append(diccCarga)
                cargar = input(f"\n\tDesea cargar otro registro? s/n: ")

            return sobreescribeArchivo(nombreNew, listaCarga)




        if int(menuCarga)== 3:
            print("Volvemos a menu principal")
            return

        else: print("No es una opcion valida de menu.. ") # evalua las entradas de menu archivo existente y retorna a menu principal


    else:
        while cargar != "n":
            diccCarga = {"Total Vacaciones":0}
            for i in cabecera:
                diccCarga[i] = (input(f"\n\tIngrese {i}: "))
                try:
                    int(diccCarga["Legajo"])
                    int(diccCarga["Total Vacaciones"])

                except:
                    print("\n\tLegajo y vacaciones debe ser un numero.")
                    return

            listaCarga.append(diccCarga)
            cargar = input(f"\n\tDesea cargar otro registro? s/n: ")

        return creaArchivo(nombreNew,listaCarga)


# ------- Funcion recibe nombre de archivo a aparear y legajo a buscar.

def consultarVacaciones(archivo, basedatos,legajoBuscado):
    try:
        with open(archivo) as fArchivo, open(basedatos) as fDatos:
            archivoCsv = csv.reader(fArchivo, delimiter = ",")
            datosCsv = csv.reader(fDatos, delimiter = ",")


            next(archivoCsv)
            next(datosCsv)

            legajo = next(archivoCsv, None)
            dia = next(datosCsv, None)

            empleado = ""
            vacacionesTomadas = 0
            vacaciones = 0
            existe = False


            while legajo: # mietras exista linea con legajo

                if legajoBuscado != legajo[0]: # buscamos coincidencia en los legajos apareados
                    dia = next(datosCsv, None) # avanza de linea si no coincide


                if int(legajo[0]) == legajoBuscado: # si legajo del archivo coincide
                    empleado = (f"{legajo[2]} {legajo[1]}") # slavamos nombre de empleado
                    vacaciones = int(legajo[3]) # Tomamos de archvo los dias a los que corresponde vacaciones
                    existe = True # Afirma que existe el legajo.

                    while dia:

                        if int(dia[0])==legajoBuscado: # evaluo que coincide con el legajo buscado
                            print(f"tomó en fecha: {dia[1]}")
                            vacacionesTomadas += 1  # sumo un dia pot coincidencia
                        dia = next(datosCsv, None) # avanzo de linea en archivo datosCsv

                legajo = next(archivoCsv, None) # avanzo de linea en archivo cosnultado

            if existe == False:
                print("El legajo buscado no existe.")
                return
            if (vacaciones-vacacionesTomadas) < 0:
                print(f"\t\n{empleado} ha excedido por ", vacacionesTomadas - vacaciones  ," dias sus vacaciones.\n")
            else:
                print(f"\t\nA {empleado} le restan ", vacaciones - vacacionesTomadas ," dias de vacaciones.\n")


    except FileNotFoundError: # atrapo except en caso de no poder abrir archivo por error en nombre o por que no existe
        print(f"\t{archivo}, no existe.\n")
        return




def principal():
    salir = ""
    while salir != "s":

        try:
            print (f"\nMENU PRINCIPAL: 1: Cargar vacaciones.\n\t\t2: Consultar vacaciones.\n\t\t3: salir.")
            menu = int(input("\t\t : "))

            if menu == 1:
                cargarVacaciones()

            if menu == 2:
                print("\tIngrese nombre del archivo a aparear sin la extension .csv:")
                nombreArchivo = input("\t")
                print("\tIngrese numero de legajo que quiere consultar: ")

                try:
                    numeroLegajo = int(input("\t")) # evaluo que sea un entero el jegajo a buscar
                    consultarVacaciones(f'{nombreArchivo}.csv','dias.csv',numeroLegajo)

                except ValueError:
                    print("\tLegajo debe ser un entero, intenta de nuevo\n")

            if menu == 3:
                salir = "s"

        except ValueError:
            print("\n\t\tNo es una entrada valida de menu.")
            return principal()

principal()
