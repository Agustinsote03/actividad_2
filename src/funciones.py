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
    
    
    

