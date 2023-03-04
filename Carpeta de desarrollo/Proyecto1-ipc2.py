#Proyecto1-ipc2
# import os

# def generar_tabla(largo, ancho, organismos):
#     imprimirPag = '''
#     graph main {
#     '''
#     if largo <= 10000 and ancho <= 10000:
#         try:
#             s = '''nodo1 [shape=plaintext, label=<
#                         <table border="2" cellborder="1" cellspacing="7">
#                 '''

#             n = 0
#             for i in range(0, largo + 1):
#                 m = 0
#                 s2 = '''
#                 <tr>
#                 '''
#                 s += s2
#                 for j in range(0, ancho + 1):
#                     if i == 0 and j == 0:
#                         s3 = f'''
#                         <td></td>
#                         '''
#                     elif i == 0:
#                         s3 = f'''
#                         <td>{j}</td>
#                         '''
#                     elif j == 0:
#                         s3 = f'''
#                         <td>{i}</td>
#                         '''
#                     else:
#                         s3 = f'''
#                         <td>{organismos.get((i, j), "")}</td>
#                         '''
#                     s += s3
#                     m += 1
#                 s4 = '''
#                 </tr>
#                 '''
#                 s += s4
#                 n += 1

#             s5 = '''
#                 </table>>]
#             '''
#             s6 = '}'

#             with open('Bacterias.dot', 'w') as f:
#                 f.write(imprimirPag)
#                 f.write(s)
#                 f.write(s5)
#                 f.write(s6)

#             os.system('dot -Tpdf Bacterias.dot -o Bacterias.pdf')

#         except:
#             print("Ocurrio un Error")
#     else:
#         print("Ha ingresado un numero invalido de columnas o Filas")

# print("Generar Tabla")
# print("-------------")

# organismos = {}  # diccionario para almacenar los organismos en las celdas de la tabla
# seleccionar_tamanio = True  # variable que indica si el usuario ya ingreso el tamanio de la tabla

# while seleccionar_tamanio:
#     largo = int(input("Ingrese el largo de la tabla: "))
#     ancho = int(input("Ingrese el ancho de la tabla: "))
#     print("")
#     if largo <= 0 or ancho <= 0:
#         print("El largo y el ancho deben ser mayores que cero.")
#         continue
#     seleccionar_tamanio = False
#     organismos_disponibles = ["Organismo A", "Organismo B ", "Organismo C", "Organismo D"]
#     while True:
#         print("¿Qué desea hacer?")
#         print("1. Agregar organismo")
#         print("2. Ver tabla")
#         opcion = input()
#         if opcion == "1":
#             while True:
#                 print("Seleccione la celda:")
#                 fila = int(input("Fila: "))
#                 columna = int(input("Columna: "))
#                 if 1 <= fila <= largo and 1 <= columna <= ancho:
#                     break
#                 else:
#                     print("Celda inválida, intente de nuevo.")
#             while True:
#                 print("Seleccione el organismo:")
#                 for i, org in enumerate(organismos_disponibles):
#                     print(f"{i + 1}. {org}")
#                 org_seleccionado = input()
#                 if org_seleccionado in ["1", "2", "3", "4"]:
#                     organismos[(fila, columna)] = organismos_disponibles[int(org_seleccionado) - 1]
#                     break
#                 else:
#                     print("Organismo inválido, intente de nuevo.")
#         elif opcion == "2":
#             generar_tabla(largo, ancho, organismos)
#             os.system('open Bacterias.pdf')
#         else:
#             print("Opción inválida, intente de nuevo.")

# import os

# def generar_tabla(largo, ancho, organismos):
#     imprimirPag = '''
#     graph main {
#     '''
#     if largo <= 10000 and ancho <= 10000:
#         try:
#             s = '''nodo1 [shape=plaintext, label=<
#                         <table border="2" cellborder="1" cellspacing="7">
#                 '''

#             n = 0
#             for i in range(0, largo + 1):
#                 m = 0
#                 s2 = '''
#                 <tr>
#                 '''
#                 s += s2
#                 for j in range(0, ancho + 1):
#                     if i == 0 and j == 0:
#                         s3 = f'''
#                         <td></td>
#                         '''
#                     elif i == 0:
#                         s3 = f'''
#                         <td>{j}</td>
#                         '''
#                     elif j == 0:
#                         s3 = f'''
#                         <td>{i}</td>
#                         '''
#                     else:
#                         org = organismos.get((i, j), {"organismo": "", "estado": " "})
#                         s3 = f'''
#                         <td>{org["organismo"]}({org["estado"]})</td>
#                         '''
#                     s += s3
#                     m += 1
#                 s4 = '''
#                 </tr>
#                 '''
#                 s += s4
#                 n += 1

#             s5 = '''
#                 </table>>]
#             '''
#             s6 = '}'

#             with open('Bacterias.dot', 'w') as f:
#                 f.write(imprimirPag)
#                 f.write(s)
#                 f.write(s5)
#                 f.write(s6)

#             os.system('dot -Tpdf Bacterias.dot -o Bacterias.pdf')

#         except:
#             print("Ocurrio un Error")
#     else:
#         print("Ha ingresado un numero invalido de columnas o Filas")

# print("Generar Tabla")
# print("-------------")

# organismos = {}  # diccionario para almacenar los organismos en las celdas de la tabla
# seleccionar_tamanio = True  # variable que indica si el usuario ya ingreso el tamanio de la tabla

# while seleccionar_tamanio:
#     largo = int(input("Ingrese el largo de la tabla: "))
#     ancho = int(input("Ingrese el ancho de la tabla: "))
#     print("")
#     if largo <= 0 or ancho <= 0:
#         print("El largo y el ancho deben ser mayores que cero.")
#         continue
#     seleccionar_tamanio = False
#     organismos_disponibles = [{"nombre": "Organismo A", "estado": "viva"}, 
#                               {"nombre": "Organismo B", "estado": "viva"},
#                               {"nombre": "Organismo C", "estado": "viva"}, 
#                               {"nombre": "Organismo D", "estado": "viva"}]
#     while True:
#         print("¿Qué desea hacer?")
#         print("1. Agregar organismo")
#         print("2. Ver tabla")
#         opcion = input()
#         if opcion == "1":
#             while True:
#                 print("Organismos disponibles:")
#                 for i, org in enumerate(organismos_disponibles):
#                     print(f"{i + 1}. {org['nombre']} ({org['estado']})")
#                 seleccion = input("Seleccione el organismo que desea agregar (1-4): ")
#                 try:
#                     seleccion = int(seleccion)
#                     if seleccion < 1 or seleccion > 4:
#                         print("Debe seleccionar un organismo disponible.")
#                         continue
#                     break
#                 except ValueError:
#                     print("Debe seleccionar un organismo disponible.")
#                     continue
#             estado = input("¿Vivo o muerto? ")
#             if estado.lower() not in ("vivo", "muerto"):
#                 print("Debe ingresar 'vivo' o 'muerto'.")
#                 continue
#             fila = int(input("Ingrese la fila en la que desea agregar el organismo: "))
#             columna = int(input("Ingrese la columna en la que desea agregar el organismo: "))
#             if fila < 1 or fila > largo or columna < 1 or columna > ancho:
#                 print(f"La fila debe estar entre 1 y {largo} y la columna debe estar entre 1 y {ancho}.")
#                 continue
#             organismo = organismos_disponibles[seleccion - 1]["nombre"]
#             organismos[(fila, columna)] = {"organismo": organismo, "estado": estado}
#             print(f"Se ha agregado {organismo} ({estado}) a la celda ({fila}, {columna}).")
#         elif opcion == "2":
#             generar_tabla(largo, ancho, organismos)
#         else:
#             print("Opción no válida.")



import os
import xml.etree.ElementTree as ET

def generar_tabla(largo, ancho, organismos):
    imprimirPag = '''
    graph main {
    '''
    if largo <= 10000 and ancho <= 10000:
        try:
            s = '''nodo1 [shape=plaintext, label=<
                        <table border="2" cellborder="1" cellspacing="7">
                '''

            n = 0
            for i in range(0, largo + 1):
                m = 0
                s2 = '''
                <tr>
                '''
                s += s2
                for j in range(0, ancho + 1):
                    if i == 0 and j == 0:
                        s3 = f'''
                        <td></td>
                        '''
                    elif i == 0:
                        s3 = f'''
                        <td>{j}</td>
                        '''
                    elif j == 0:
                        s3 = f'''
                        <td>{i}</td>
                        '''
                    else:
                        org = organismos.get((i, j), {"organismo": "", "estado": " "})
                        s3 = f'''
                        <td>{org["organismo"]}({org["estado"]})</td>
                        '''
                    s += s3
                    m += 1
                s4 = '''
                </tr>
                '''
                s += s4
                n += 1

            s5 = '''
                </table>>]
            '''
            s6 = '}'

            with open('Bacterias.dot', 'w') as f:
                f.write(imprimirPag)
                f.write(s)
                f.write(s5)
                f.write(s6)

            os.system('dot -Tpdf Bacterias.dot -o Bacterias.pdf')

        except:
            print("Ocurrio un Error")
    else:
        print("Ha ingresado un numero invalido de columnas o Filas")

# def crear_XML(listaOrganismos, listadoMuestras):
#     root = ET.Element("datosMarte")
#     lista_org = ET.SubElement(root, "listaOrganismos")
#     for org in listaOrganismos:
#         org_elem = ET.SubElement(lista_org, "organismo")
#         codigo = ET.SubElement(org_elem, "codigo")
#         codigo.text = org["codigo"]
#         nombre = ET.SubElement(org_elem, "nombre")
#         nombre.text = org["nombre"]
#     listado_muestras = ET.SubElement(root, "listadoMuestras")
#     for muestra in listadoMuestras:
#         muestra_elem = ET.SubElement(listado_muestras, "muestra")
#         codigo = ET.SubElement(muestra_elem, "codigo")
#         codigo.text = muestra["codigo"]
#         descripcion = ET.SubElement(muestra_elem, "descripcion")
#         descripcion.text = muestra["descripcion"]
#         filas = ET.SubElement(muestra_elem, "filas")
#         filas.text = str(muestra["filas"])
#         columnas = ET.SubElement(muestra_elem, "columnas")
#         columnas.text = str(muestra["columnas"])
#         listado_celdas = ET.SubElement(muestra_elem, "listadoCeldasVivas")
#         for celda in muestra["celdas_vivas"]:
#             celda_elem = ET.SubElement(listado_celdas, "celdaViva")
#             fila = ET.SubElement(celda_elem, "fila")
#             fila.text = str(celda[0])
#             columna = ET.SubElement(celda_elem, "columna")
#             columna.text = str(celda[1])
#     return ET.tostring(root)

def cargar_XML():
    nombre_archivo = input("Ingrese el nombre del archivo XML a cargar: ")
    try:
        arbol = ET.parse(nombre_archivo)
        raiz = arbol.getroot()

        lista_organismos = []
        lista_muestras = []

        for elem in raiz.iter("organismo"):
            codigo = elem.find("codigo").text
            nombre = elem.find("nombre").text
            lista_organismos.append({"codigo": codigo, "nombre": nombre})

        for elem in raiz.iter("muestra"):
            codigo = elem.find("codigo").text
            descripcion = elem.find("descripcion").text
            filas = int(elem.find("filas").text)
            columnas = int(elem.find("columnas").text)
            celdas_vivas = []
            for celda in elem.iter("celdaViva"):
                fila = int(celda.find("fila").text)
                columna = int(celda.find("columna").text)
                celdas_vivas.append((fila, columna))
            lista_muestras.append({"codigo": codigo, "descripcion": descripcion, "filas": filas, "columnas": columnas, "celdas_vivas": celdas_vivas})

        return (lista_organismos, lista_muestras)

    except:
        print("No se pudo cargar el archivo XML")

def agregar_organismo_manual(organismos):
    codigo = input("Ingrese el codigo del organismo: ")
    nombre = input("Ingrese el nombre del organismo: ")
    organismos.append({"codigo": codigo, "nombre": nombre})

def menu():
    organismos = []
    muestras = []

    while True:
        print("MENU")
        print("1. Cargar archivo XML")
        print("2. Agregar organismo manualmente")
        print("3. Generar tabla")
        print("4. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            resultado = cargar_XML()
            if resultado is not None:
                organismos, muestras = resultado
                print("Archivo cargado exitosamente.")
        elif opcion == 2:
            agregar_organismo_manual(organismos)
        elif opcion == 3:
            if muestras:
                muestra_seleccionada = None
                while muestra_seleccionada is None:
                    print("Muestras disponibles:")
                    for i, muestra in enumerate(muestras):
                        print(f"{i+1}. {muestra['descripcion']}")
                    seleccion = int(input("Seleccione una muestra: "))
                    if seleccion > 0 and seleccion <= len(muestras):
                        muestra_seleccionada = muestras[seleccion-1]
                    else:
                        print("Seleccion invalida.")
                generar_tabla(muestra_seleccionada["filas"], muestra_seleccionada["columnas"], {(c[0], c[1]): {"organismo": " ", "estado": " "} for c in muestra_seleccionada["celdas_vivas"]})
            else:
                print("No hay muestras disponibles.")
        elif opcion == 4:
            break
        else:
            print("Opcion invalida.")

menu()
