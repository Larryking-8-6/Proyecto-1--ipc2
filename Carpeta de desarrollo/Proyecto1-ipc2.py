tabla = {}
muestra_seleccionada = {"filas": 5, "columnas": 5}
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

import xml.etree.ElementTree as ElementTree

def exportar_XML():
    if tabla:
        archivo = input("Ingrese el nombre del archivo a guardar: ")
        juego = ElementTree.Element("juego")
        for celda, estado_org in tabla.items():
            fila, columna = celda
            codigo_org = estado_org["organismo"]
            estado = estado_org["estado"]
            celula = ElementTree.Element("celula", {"fila": str(fila), "columna": str(columna), "organismo": codigo_org, "estado": estado})
            juego.append(celula)
        tree = ElementTree.ElementTree(juego)
        tree.write(archivo + ".xml")
        print("Archivo guardado exitosamente.")
    else:
        print("No hay tabla para exportar.")

def agregar_organismo_manual():
    global tabla
    print("Celdas disponibles:")
    for fila in range(1, muestra_seleccionada["filas"]+1):
        for columna in range(1, muestra_seleccionada["columnas"]+1):
            if (fila, columna) not in tabla:
                print(f"({fila}, {columna})")
    fila = int(input("Ingrese la fila donde desea agregar el organismo: "))
    columna = int(input("Ingrese la columna donde desea agregar el organismo: "))
    codigo = input("Ingrese el código del organismo: ")
    tabla[(fila, columna)] = {"organismo": f"{codigo}", "estado": "V"}
    
    # Actualizar estado de celdas adyacentes
    for celda in adyacentes((fila, columna)):
        if celda in tabla:
            tabla[celda]["estado"] = "A"
            
    generar_tabla(muestra_seleccionada["filas"], muestra_seleccionada["columnas"], tabla)

def adyacentes(celda):
    fila, col = celda
    adyacentes = [(fila-1, col-1), (fila-1, col), (fila-1, col+1),
                  (fila, col-1),                 (fila, col+1),
                  (fila+1, col-1), (fila+1, col), (fila+1, col+1)]
    # agregamos las celdas con organismos agregados manualmente a los adyacentes
    adyacentes += [(f, c) for f, c in [(fila-1, col-1), (fila-1, col), (fila-1, col+1),
                  (fila, col-1),                 (fila, col+1),
                  (fila+1, col-1), (fila+1, col), (fila+1, col+1)]
                   if (f, c) not in adyacentes and (f, c) in tabla and tabla[(f, c)]["organismo"] != " "]
    return adyacentes

def menu():
    global tabla
    muestra_seleccionada = None
    organismos = []
    muestras = []
    num_generacion = 0
    tabla = {}
    organismo_seleccionado = None
    codigo = ""
    

    while True:
        print("MENU")
        print("")
        print("1. Cargar archivo XML")
        print("2. Generar tabla")
        print("3. Agregar organismo manualmente")
        print("4. Cargar organismos disponibles")
        print("5. Datos de comida")
        print("6. Accion del programa")
        print("7. Exportar xml")
        print("8. Salir")
        print("")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            resultado = cargar_XML()
            if resultado is not None:
                organismos, muestras = resultado
                print("Archivo cargado exitosamente.")
        elif opcion == 2:
            if muestras:
                muestra_seleccionada = None
                while muestra_seleccionada is None:
                    print("Muestras disponibles:")
                    for i, muestra in enumerate(muestras):
                        print(f"{i+1}. {muestra['descripcion']}")
                    seleccion = int(input("Seleccione una muestra: "))
                    if seleccion > 0 and seleccion <= len(muestras):
                        muestra_seleccionada = muestras[seleccion-1]
                        tabla = {(c[0], c[1]): {"organismo": " ", "estado": " "} for c in muestra_seleccionada["celdas_vivas"]}
                    else:
                        print("Seleccion invalida.")
                generar_tabla(muestra_seleccionada["filas"], muestra_seleccionada["columnas"], tabla)
            else:
                print("No hay muestras disponibles.")
        elif opcion == 3:
            agregar_organismo_manual()
            generar_tabla(muestra_seleccionada["filas"],muestra_seleccionada["columnas"], tabla)
        elif opcion == 4:
            if organismos:
                print("Cargando todos los organismos disponibles...")
                # obtener celdas disponibles
                celdas_disponibles = [(fila, columna) for fila, columna in muestra_seleccionada["celdas_vivas"] if tabla[(fila, columna)]["organismo"] == " "]
                for i, organismo in enumerate(organismos):
                    if i >= len(celdas_disponibles):
                        break  # no hay más celdas disponibles
                    codigo_org = organismo['codigo']
                    celda = celdas_disponibles[i]
                    tabla[celda]["organismo"] = codigo_org
                    tabla[celda]["estado"] = "V"
                    print(f"Código de organismo {codigo_org} asignado a la celda ({celda[0]}, {celda[1]})")
                generar_tabla(muestra_seleccionada["filas"], muestra_seleccionada["columnas"], tabla)
            else:
                print("No hay organismos disponibles.")
                
        elif opcion == 5:
            if tabla:
                print("Organismos cargados:")
                for celda, estado_org in tabla.items():
                    fila, columna = celda
                    if estado_org["organismo"] != " ":
                        codigo_org = estado_org["organismo"]
                        estado = estado_org["estado"]
                        print(f"Código de organismo: {codigo_org} - Posición: ({fila}, {columna}) - Estado: {estado}")
            else:
                print("No hay organismos cargados.")

        elif opcion == 6:
            while True:
                print("MINI MENU")
                print("1. Comer")
                print("2. Ver estado de todos los organismos")
                print("3. Regresar al menu")
                accion = int(input("Seleccione una opcion: "))

                if accion == 1:
                    print("Acción comer seleccionada")
                    opcion = input("Desea seleccionar un organismo de la tabla? (S/N): ")
                    if opcion.upper() == "S":
                        lista_organismos = [tabla[celda]["organismo"] for celda in tabla if tabla[celda]["organismo"] != " "]
                        if lista_organismos:
                            print("Organismos disponibles en la tabla:")
                            for i, organismo in enumerate(lista_organismos):
                                print(f"{i+1}. {organismo}")
                            opcion_org = int(input("Seleccione el organismo que desea mover: "))
                            organismo_seleccionado = lista_organismos[opcion_org-1]
                            celdas_organismo = [celda for celda in tabla if tabla[celda]["organismo"] == organismo_seleccionado]
                            if celdas_organismo:
                                pos_org = celdas_organismo[0]
                            else:
                                print(f"No se encontró el organismo {organismo_seleccionado} en la tabla.")
                                continue
                        else:
                            print("No hay organismos en la tabla para seleccionar.")
                            continue
                    else:
                        fila_org = int(input("Ingrese la fila del organismo que desea mover: "))
                        col_org = int(input("Ingrese la columna del organismo que desea mover: "))
                        pos_org = (fila_org, col_org)
                    if pos_org in tabla:
                        if tabla[pos_org]["organismo"] != " ":
                            organismo_seleccionado = tabla[pos_org]["organismo"]
                            # obtener las celdas ocupadas por el organismo seleccionado
                            celdas_organismo = [celda for celda in tabla if tabla[celda]["organismo"] == organismo_seleccionado]
                        # actualizar la información en cada una de las celdas ocupadas por el organismo seleccionado y las celdas adyacentes a éstas
                        celdas_modificadas = celdas_organismo.copy()
                        for celda in celdas_organismo:
                            tabla[celda]["organismo"] = organismo_seleccionado
                            tabla[celda]["num_generacion"] = num_generacion
                            for adyacente in adyacentes(celda):
                                if adyacente in tabla:
                                    if tabla[adyacente]["organismo"] == " ":
                                        tabla[adyacente]["organismo"] = organismo_seleccionado
                                        tabla[adyacente]["num_generacion"] = num_generacion
                                        celdas_modificadas.append(adyacente)
                                        
                                    else:  # Si la celda adyacente ya está ocupada, copiar el organismo seleccionado en ella
                                        tabla[adyacente]["organismo"] = organismo_seleccionado
                                        tabla[adyacente]["num_generacion"] = num_generacion
                                        celdas_modificadas.append(adyacente)
                                        print(f"Puede salvarse en la celda {adyacente} donde esta {tabla[adyacente]['organismo']}, que ha sido comido por el organismo seleccionado.")
                        
                        # obtener las celdas adyacentes que ya están ocupadas
                        ocupadas = [celda for celda in adyacentes(pos_org) if celda in tabla and tabla[celda]["organismo"] != " "]

                        # revertir los cambios
                        for celda in celdas_modificadas:
                            if celda not in celdas_organismo and celda not in ocupadas:
                                tabla[celda]["organismo"] = " "
                                tabla[celda]["num_generacion"] = -1
                    generar_tabla(muestra_seleccionada["filas"], muestra_seleccionada["columnas"], tabla)
                    #return tabla, num_generacion
                    
                elif accion == 2:
                    print("Estado de todos los organismos:")
                    for celda, estado_org in tabla.items():
                        fila, columna = celda
                        if estado_org["organismo"] != " ":
                            codigo_org = estado_org["organismo"]
                            estado = estado_org["estado"]
                            print(f"Código de organismo: {codigo_org} - Posición: ({fila}, {columna}) - Estado: {estado}")
                elif accion == 3:
                    break
                else:
                    print("Opcion invalida.")
        elif opcion == 7:
            exportar_XML()
            break

        elif opcion == 8:
            print("Has salido del programa tenga buen dia.")
            print("")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

menu()