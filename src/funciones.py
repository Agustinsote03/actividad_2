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
    
    return {"Palabras por línea: " : prom_palabras, "Cantidad de líneas: " : cant_lineas, "Cantidad de palabras: " : cant_palabras}

