import csv
import os.path


def creaArchivo(nombre, lista):
    cabecera = ["Legajo", "Apellido" , "Nombre" , "Total Vacaciones"]

    with open(f"{nombre}.csv", "w") as newF:
        newFile = csv.DictWriter(newF,fieldnames=cabecera)

        newFile.writeheader()
        newFile.writerows(lista)


    print(f"\t{nombre}.csv ha sido creado con exito. ")
    return



def cargarVacaciones():
    nombreNew = input("\t\nNombre para el archivo .csv: ")
    cabecera = ["Legajo", "Apellido" , "Nombre" , "Total Vacaciones"]
    listaCarga =[]
    cargar = ""

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

                if legajoBuscado != legajo[0]:
                    dia = next(datosCsv, None)


                if int(legajo[0]) == legajoBuscado: # si legajo del archivo coincide con el de la busqueda
                    empleado = (f"{legajo[2]} {legajo[1]}")
                    vacaciones = int(legajo[3])
                    existe = True

                    while dia:

                        if int(dia[0])==legajoBuscado: # evaluo que coincide con el legajo buscado
                            print(f"tomó en fecha: {dia[1]}")
                            vacacionesTomadas += 1  # sumo los valores que estan en el index 1 de gastos
                        dia = next(datosCsv, None) # paso de linea en archivo gastos

                legajo = next(archivoCsv, None)

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
