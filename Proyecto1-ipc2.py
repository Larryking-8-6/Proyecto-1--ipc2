#Proyecto1-ipc2

# import codecs
# import os

# def generate_graph():
#     hojab = ''' 
#     digraph main {
#     graph [pad="0.5", nodesep="0.5", ranksep="2"];
#     node [shape=plain]
#     rankdir=LR;\n
#     '''

#     # Nodos de películas
#     for i in range(14):
#         movie_node = f'nodo{i} [label=<<table border="0" cellborder="1" cellspacing="0"><tr><td colspan="3" bgcolor="#0891ea">{f"Pelicula {i+1}"}</td></tr><tr><td>Anio</td><td>Genero</td></tr></table>>];\n'
#         hojab += movie_node

#     # Nodos de actores
#     for i in range(18):
#         actor_node = f'actor{i} [label=<<table border="0" cellborder="1" cellspacing="0"><tr><td bgcolor="#f7dc6f">{f"Actor {i+1}"}</td></tr></table>>];\n'
#         hojab += actor_node

#     # Conexiones de películas a actores
#     for i in range(14):
#         for j in range(18):
#             movie_node = f'nodo{i}'
#             actor_node = f'actor{j}'
#             hojab += f'{movie_node}:p1 -> {actor_node};\n'

#     hojafin = '}'
#     with codecs.open('Matriz.dot', 'w', 'utf-8') as f:
#         f.write(hojab)
#         f.write(hojafin)

#     os.system('dot -Tpdf Matriz.dot -o Matriz.pdf')

# generate_graph()

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from PIL import Image
# import io

# img_width = 1000
# img_height = 1000

# def generate_graph():
#     hojab = ''
    
#     # Nodos de películas
#     for i in range(14):
#         movie_node = f' A {i+1} '
#         hojab += f'┌{"─" * 17}┐'
#     hojab += '┐\n'
    
#     # Separador de fila superior
#     separator_top = '│' + '┬'.join(['─' * 17] * 14) + '│\n'
#     hojab += separator_top

#     # Nodos de actores y conexiones a películas
#     for i in range(18):
#         hojab += '│'
#         for j in range(14):
#             actor_node = f' Bacteria '
#             hojab += f' {actor_node:<17}│'
#         hojab += '\n'

#         # Separador de fila intermedia
#         if i < 17:
#             separator_mid = '│' + '┼'.join(['─' * 17] * 14) + '│\n'
#             hojab += separator_mid
    
#     # Separador de fila inferior
#     separator_bot = '│' + '┴'.join(['─' * 17] * 14) + '│\n'
#     hojab += separator_bot

#     # Margen alrededor de la matriz
#     margin = 2
#     hojab = ' ' * margin + hojab.replace('\n', '\n' + ' ' * margin)

#     # Guardar la imagen generada en un buffer
#     img_buffer = io.BytesIO()
#     img = Image.frombytes("RGB", (img_width, img_height), hojab.encode())
#     img.save(img_buffer, format='png')
#     img_buffer.seek(0)

#     # Imprimir el tamaño de la imagen cargada
#     print(img.size)

#     # Generar PDF y añadir imagen
#     pdf_canvas = canvas.Canvas("graph.pdf", pagesize=letter)
#     pdf_canvas.drawImage(img_buffer, x=0, y=letter[1] - img_height)
#     pdf_canvas.showPage()
#     pdf_canvas.save()

# generate_graph()

#Menu principal
def print_menu():
    print("Menu de opciones:")
    print("1. Cargar archivo de entrada")
    print("2. Gestionar películas")
    print("3. Filtrado")
    print("4. Gráfica")
    print("5. Salir")


import codecs
import os

def generate_graph():
    hojab = ''
    
    # Nodos de películas
    for i in range(11):
        movie_node = f' A {i+1} '
        hojab += f'┌{"─" * 17}┐'
    hojab += '┐\n'
    
    # Separador de fila superior
    separator_top = '│' + '┬'.join(['─' * 17] * 14) + '│\n'
    hojab += separator_top

    # Nodos de actores y conexiones a películas
    for i in range(18):
        hojab += '│'
        for j in range(14):
            actor_node = f' Bacteria '
            hojab += f' {actor_node:<17}│'
        hojab += '\n'

        # Separador de fila intermedia
        if i < 17:
            separator_mid = '│' + '┼'.join(['─' * 17] * 14) + '│\n'
            hojab += separator_mid
    
    # Separador de fila inferior
    separator_bot = '│' + '┴'.join(['─' * 17] * 14) + '│\n'
    hojab += separator_bot

    # Margen alrededor de la matriz
    margin = 2
    hojab = ' ' * margin + hojab.replace('\n', '\n' + ' ' * margin)

    print(hojab)

    hojafin = '}'
    with codecs.open('Pruebas.dot', 'w','utf-8') as f:
        f.write(hojab)
        f.write(hojafin)

    os.system('dot -Tpdf Pruebas.dot -o Pruebas.pdf')
# generate_graph()



