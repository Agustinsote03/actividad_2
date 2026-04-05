#-------------------------FUNCIONES AUXILIARES-------------------------#

def convertir_duracion_a_segundos(duracion):
    """
     recibe un string con formato "m:ss" y retorna la duración total en segundos (enteros)
    """
    duracion_enteros = duracion.split(":")

    #Se pasa todo a segundos
    total_segundos = int(duracion_enteros[0]) * 60 + int(duracion_enteros[1])

    return total_segundos




#-------------------------EJERCICIO 1-------------------------#

def procesar_texto(texto):
    """
    La función recibe el texto contenido en el string, lo separa en saltos de linea que guarda en la lista 'lista_lineas' y por cada elementos de la
    lista se itera contando las palabras y sumandolas a la variable acumuladora 'cant_palabras'.
    """
    #Separamos el texto por saltos de linea, se obtiene una lista donde cada elemento es un string(linea)

    lista_lineas = texto.split("\n")

    cant_lineas = len(lista_lineas)
    cant_palabras = 0

    for linea in lista_lineas:
        palabras = linea.split()
        cant_palabras += len(palabras)

    prom_palabras = cant_palabras / cant_lineas

   #Se usa una función filter aprovechando la variable 'prom_palabras'. Usamos una función lambda para comprar cada palabra de la linea con linea.split()

    lista_filtrada_por_promedio = list(filter(lambda linea: len(linea.split()) > prom_palabras, lista_lineas))

    #Este bloque se encarga de imprimir los resultados 

    print(f"Cantidad de lineas: {cant_lineas}")
    print(f"Cantidad de palabras: {cant_palabras}")
    print(f"Promedio de palabras por linea: {prom_palabras}")
    print(" ")
    print("Líneas por encima del promedio (7.21 palabras): ")
    for linea in lista_filtrada_por_promedio:
        print(f"-{linea}")



#-------------------------EJERCICIO 2-------------------------#

def procesar_playlist(playlist):
    """
     La función calcule e imprime la duración total de la playlist y halla e imprime la canción más larga y la más corta.
    """

    #Pasamos todo a segundos utilizando map() y lambda con una función auxiliar 'convertir_duracion_a_segundos' y lo guardamos en 'lista_segundos'
    lista_segundos = list(map(lambda cancion: convertir_duracion_a_segundos(cancion["duration"]), playlist))
    total_segundos = sum(lista_segundos)

    #Se convierte los segundos totales al formato Xm Ys

    minutos = total_segundos // 60
    segundos = total_segundos % 60

    #Este bloque busca la canción más larga y la más corta usando map(), y una lambda aprovechando la funcion auxiliar de conversion a segundos

    mas_larga = max(playlist, key = lambda cancion: convertir_duracion_a_segundos(cancion["duration"]))
                            
    mas_corta = min(playlist, key = lambda cancion: convertir_duracion_a_segundos(cancion["duration"]))
    
    #Este bloque imprime los resultados
    
    print(f"Duracion total: {minutos}m {segundos}s")
    print(f"Canción más larga: {mas_larga["title"]} {mas_larga["duration"]}")
    print(f"Canción más corta: {mas_corta["title"]} {mas_corta["duration"]}")


#-------------------------EJERCICIO 3-------------------------#

def filtrar_spoilers(review):
    """
       Esta función solicita las palabras spoiler y las reempleza por asteriscos en la reseña
    """

    # Se solicitan las palabras consideradas spoiler
    entrada = input("Ingrese las palabras spoiler separadas por comas: ")

    #Se crea una lista de palabras spoiler a partir de la entrada del usuario y se la normaliza quitando espacios y pasando a minuscula con map() y lambda
    palabras_spoiler = entrada.split(",")
    lista_de_spoilers = list(map(lambda palabra: palabra.strip().lower(), palabras_spoiler))

    #Se itera por cada palabra de la reseña con review.split(), usando map() y lambda(). Se censura con '*' cada letra de la palabra si coincide con alguna de las palabras spoiler de la lista
    resultado = list(map(lambda palabra: "*" * len(palabra) if palabra.lower() in lista_de_spoilers else palabra, review.split()))

    #Se unen las palabras de la reseña con espacios y se imprime el texto con las palabras spoiler censuradas

    texto_censurado = " ".join(resultado)
    print()
    print(texto_censurado)
    

