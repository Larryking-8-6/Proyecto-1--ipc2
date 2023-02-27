#Proyecto1-ipc2
import os

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
                        s3 = f'''
                        <td>{organismos.get((i, j), "")}</td>
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

print("Generar Tabla")
print("-------------")

organismos = {}  # diccionario para almacenar los organismos en las celdas de la tabla
seleccionar_tamanio = True  # variable que indica si el usuario ya ingreso el tamanio de la tabla

while seleccionar_tamanio:
    largo = int(input("Ingrese el largo de la tabla: "))
    ancho = int(input("Ingrese el ancho de la tabla: "))
    print("")
    if largo <= 0 or ancho <= 0:
        print("El largo y el ancho deben ser mayores que cero.")
        continue
    seleccionar_tamanio = False
    organismos_disponibles = ["Organismo A", "Organismo B", "Organismo C", "Organismo D"]
    while True:
        print("¿Qué desea hacer?")
        print("1. Agregar organismo")
        print("2. Ver tabla")
        opcion = input()
        if opcion == "1":
            while True:
                print("Seleccione la celda:")
                fila = int(input("Fila: "))
                columna = int(input("Columna: "))
                if 1 <= fila <= largo and 1 <= columna <= ancho:
                    break
                else:
                    print("Celda inválida, intente de nuevo.")
            while True:
                print("Seleccione el organismo:")
                for i, org in enumerate(organismos_disponibles):
                    print(f"{i + 1}. {org}")
                org_seleccionado = input()
                if org_seleccionado in ["1", "2", "3", "4"]:
                    organismos[(fila, columna)] = organismos_disponibles[int(org_seleccionado) - 1]
                    break
                else:
                    print("Organismo inválido, intente de nuevo.")
        elif opcion == "2":
            generar_tabla(largo, ancho, organismos)
            os.system('open Bacterias.pdf')
        else:
            print("Opción inválida, intente de nuevo.")