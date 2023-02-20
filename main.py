# # Datos de las películas
# peliculas = [    ["The Avengers", "Robert Downey Jr,Chris Evans,Chris Hemsworth", 2012, "Ficcion"],
#     ["Spiderman", "Tobey Maguire,Kirsten Dunst,Willem Dafoe", 2002, "Accion"],
#     ["The Amazing Spiderman", "Andrew Garfield,Emma Stone", 2012, "Accion"],
#     ["The Amazing Spiderman 2", "Andrew Garfield,Emma Stone", 2014, "Accion"],
#     ["Spiderman Homecoming", "Tom Holland, Zendaya", 2017, "Accion"],
#     ["Avengers Infinity War", "Robert Downey Jr,Tom Holland", 2018, "Accion"]
# ]

import graphviz

def generate_graph(movies):
    dot = graphviz.Digraph(comment='Películas')
    actors = {}  # Almacenar actores ya en el grafico
    for movie in movies:
        actor = movie['actor']
        if actor not in actors:
            # si el actor no ha sido agregado al grafico, crear un nuevo nodo para el actor
            dot.node(actor, actor, shape='box')
            actors[actor] = [movie]  # agregar actor al diccionario con la lista de peliculas
        else:
            # si el actor ya esta en el grafo, agregar la pelicula a la lista de peliculas del actor
            actors[actor].append(movie)

    for actor, movies in actors.items():
        # crear un subgrafo para cada actor y sus peliculas
        actor_node = graphviz.Digraph(name='actor_' + actor)
        for movie in movies:
            # agregar un nodo para cada pelicula con su informacion de anio y genero
            actor_node.node(movie['nombre'], label=movie['nombre'] + '\n' + str(movie['anio']) + '\n' + movie['genero'], shape='oval')
        # agregar un nodo para el actor
        actor_node.node(actor, label=actor, shape='box')
        # conectar los nodos de las peliculas correspondientes con el nodo del actor
        for movie in movies:
            actor_node.edge(actor, movie['nombre'], dir='back')
        # agregar el subgrafo de las peliculas al subgrafo del actor
        dot.subgraph(actor_node)

    dot.render('movies.gv', view=True)


#Funcion de lista para almacenar las peliculas cargadas
loaded_movies = []  

def load_movies(file_name):
    global loaded_movies  # usar la variable global
    movies = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                name, actor, year, genre = line.split(';')
                movie = {
                    'nombre': name,
                    'actor': actor,
                    'anio': int(year),
                    'genero': genre
                }
                movies.append(movie)
    loaded_movies.extend(movies)  # agregar las peliculas a la lista global
    return movies

def option1():
    file_name = input("Ingrese la ruta del archivo a cargar: ")
    movies = load_movies(file_name)
    print(f"Se cargaron {len(movies)} películas desde el archivo {file_name}.")
    input("Presione Enter para regresar al menú principal.")  # esperar la entrada del usuario para continuar

def option2(movies):
    print("")
    print("Gestion de películas")
    print("")
    print("1.Mostrar películas ")
    print("2.Mostrar actores")
    print("3.Regresar al menu")
    print("")
    choice = int(input("Elija una opción (1-3): "))
    print("")
    if choice == 1:
        print("Lista de películas:")
        for movie in movies:
            print(movie['nombre'])
    elif choice == 2:
        actors = set()
        for movie in movies:
            actors.update(movie['actor'])
        print("Lista de actores:")
        for actor in actors:
            print(actor)
    elif choice == 3:
        print("Regresando al menú principal...")
        print("")
        print("")
        print("Se encuentra en el menu principal")
        return
    else:
        print("Opción inválida. Por favor, elija una opción válida (1-3).")

#Menu del filtrado
def option3(movies):
    print("Filtrado")
    print("")
    print("1. Filtrar por actor")
    print("2. Filtrar por año")
    print("3. Filtrar por género")
    print("4. Regresar al menú principal")
    choice = int(input("Elija una opción (1-4): "))
    #Concatenacion de datos y separado
    #Nombre
    if choice == 1:
        actor = input("Ingrese el nombre del actor: ")
        filtered_movies = [movie for movie in movies if actor in movie['actor']]
        print(f"Se encontraron {len(filtered_movies)} películas con el actor {actor}:")
        for movie in filtered_movies:
            print(f"{movie['nombre']} ({movie['anio']}) - {movie['genero']}")
    
    #Anio
    elif choice == 2:
        year = int(input("Ingrese el año: "))
        filtered_movies = [movie for movie in movies if movie['anio'] == year]
        print(f"Se encontraron {len(filtered_movies)} películas del año {year}:")
        for movie in filtered_movies:
            print(f"{movie['nombre']} ({movie['actor']}) - {movie['genero']}")
    #Genero
    elif choice == 3:
        genre = input("Ingrese el género: ")
        filtered_movies = [movie for movie in movies if genre in movie['genero']]
        print(f"Se encontraron {len(filtered_movies)} películas del género {genre}:")
        for movie in filtered_movies:
            print(f"{movie['nombre']} ({movie['actor']}, {movie['anio']})")
    #Regreso al menu
    elif choice == 4:
        print("Regresando al menu principal...")
        print("")
        print("Se encuentra en el menu principal")
        return
    
    else:
        print("Opcion invalida. Por favor, elija una opción valida (1-4).")

#Funcion de seleccion para crear grafica
def option4(movies):
    print("Gráfica")
    generate_graph(movies)

#Funcion para salir
def option5():
    print("Gracias por usar el programa")

#Menu principal
def print_menu():
    print("Menu de opciones:")
    print("1. Cargar archivo de entrada")
    print("2. Gestionar películas")
    print("3. Filtrado")
    print("4. Gráfica")
    print("5. Salir")

def main():
    print("JUAN CARLOS GONZALEZ VALDEZ - 202110180")
    print("LFP (Lenguajes Formales de programacion) SECCION B+")
    print("")
    print_menu()
    print("")

    movies = []
    #Bucle del menu
    while True:
        choice = int(input("Elija una opcion (1-5): "))

        if choice == 1:
            file_name = input("Ingrese el nombre del archivo a cargar: ")
            movies = load_movies(file_name)
            print(f"Se cargaron {len(movies)} películas desde el archivo {file_name}.")
            print("")
            print_menu()
            print("")
        
        elif choice == 2:
            option2(movies)
            print("")
            print_menu()
            print("")
        
        elif choice == 3:
            option3(movies)
            print("")
            print_menu()
            print("")
        
        elif choice == 4:
            option4(movies)
            print("")
            print_menu()
            print("")
        
        elif choice == 5:
            print("")
            print("Saliendo del programa...")
            print("Gracias por usar el programa, vuelva pronto :3")
            print("")
            break
        
        else:
            print("Opción inválida. Por favor, elija una opción válida (1-5).")
            print_menu()
#Inicio de la clase
if __name__ == "__main__":
    input("Presione enter para inciar el programa...")
    main()