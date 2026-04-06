#-------------------------FUNCIONES AUXILIARES-------------------------#

def convertir_duracion_a_segundos(duracion):
    """
     recibe un string con formato "m:ss" y retorna la duración total en segundos (enteros)
    """
    duracion_enteros = duracion.split(":")

    #Se pasa todo a segundos
    total_segundos = int(duracion_enteros[0]) * 60 + int(duracion_enteros[1])

    return total_segundos

def determinar_categoria(peso):
    """
    Determina la categoría del peso según los criterios establecidos
    """
    if peso <= 1:
        return "bajo"
    elif peso <= 5:
        return "medio"
    else:
        return "alto"



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
    

#-------------------------EJERCICIO 4-------------------------#

def validar_email(email):
    """
    Valida si el email ingresado es correcto según los criterios de la cátedra utilizando métodos de cadenas
    """

    #Se verifica que contega exactamente un '@'
    if email.count("@") != 1:
        return False
    
    #Se verifica que no empiece ni termine con '@'
    cond1 = ("@",".")
    cond2 = ("@",".")
    if email.startswith(cond1) or email.endswith(cond2):
        return False
    
    #Dividimos el string en dos partes para comprobar su validez

    partes = email.split("@")
    antes_del_arroba = partes[0]
    despues_del_arroba = partes[1]
    
    #Se verifica que contiene un caracter antes del '@'
    if len(antes_del_arroba) < 1:
        return False
    
    #Se tiene en cuenta si tiene un '.' después del arroba
    if "." not in despues_del_arroba:
        return False

    #La parte después del último punto tiene al menos 2 caracteres
    partes_dominio = despues_del_arroba.split(".")
    if len(partes_dominio[-1]) < 2:
        return False
    
    return True

def solicitar_email():
    """
    Solicita al usuario un email y lo valida utilizando la función validar_email. Si el email es inválido, se le solicita nuevamente hasta que ingrese uno correcto.
    """

    email_ingresado = input("Ingrese un email: ")
    if validar_email(email_ingresado):
        print("Email válido")
    else:
        print("Email inválido. Intente nuevamente.")

#-------------------------EJERCICIO 5-------------------------#

def calcular_costo_envio(peso, zona):
    """
    -
    """
    #Se crea la tabla de precios en un diccionarios con las tarifas segun la zona y el peso
    tarifas = {
        "local": {"bajo": 500, "medio":1000, "alto":2000},
        "regional": {"bajo": 1000, "medio":2500, "alto":5000},
        "nacional": {"bajo": 2000, "medio":4500,"alto":8000}
    }

    #Normalizamos la entrada de zona
    zona = zona.strip().lower()

    #Verificamos que la zona exista
    if zona not in tarifas.keys():
        return "Zona no válida. Las opciones son: local, regional, nacional."
    
    #Se determina el costo según el peso
    categoria = determinar_categoria(peso)
    costo = tarifas[zona][categoria]

    return (f"Costo de envío: ${costo}")

def ejecutar_calculadora_envio():
    """
    Solicita los datos, los convierte al tipo correcto e imprime el resultado
    """
    
    #Se solicita el peso y la zona
    peso = float(input("Ingrese el peso del paquete en kg: "))
    zona = input("Ingrese la zona de envío (local, regional, nacional): ")

    resultado = calcular_costo_envio(peso, zona)
    print(resultado)
    
    


