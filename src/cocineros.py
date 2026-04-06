#------------------------------FUNCIONES AUXILIARES----------------------------#
def sumar_puntajes_jueces(puntaje_jueces):
    """
     Esta función toma el diccionario con las puntuaciones de los jueces y retorna la suma de ellos
    """
    total_puntos = sum(puntaje_jueces.values())
    return total_puntos

def generar_tabla_posiciones(estadisticas,cant_rondas):
    """
     Esta función genera una tabla de posiciones a partir de las estadisticas de los cocineros y 'resultados_ronda'
    """
    #Se calcula el promedio de puntos por ronda para cada cocinero
    final = []
    for (nombre, stats) in estadisticas.items():
        promedio_puntos = stats['total_puntos'] / cant_rondas
        final.append((nombre, stats['total_puntos'], stats['rondas_ganadas'], stats['mejor_ronda'], promedio_puntos))
    
    #Se ordena la tabla por 'total_puntos' de forma descendente con sorted() y lambda

    tabla_ordenada = sorted(final, key=lambda x: x[1], reverse=True)

    #Se imprime la tabla de posiciones

    print("Tabla de posiciones final:")
    print()
    print(f"{'Cocinero':<15} {'Total Puntos':<15} {'Rondas Ganadas':<15} {'Mejor Ronda':<15} {'Promedio Puntos/Ronda':<20}")
    print("-" * 80)

    for nombre_cocinero, total_puntos, rondas_ganadas, mejor_ronda, promedio in tabla_ordenada:
        print(f"{nombre_cocinero:<15} {total_puntos:<15} {rondas_ganadas:<15} {mejor_ronda:<15} {promedio:<20.2f}")


def imprimir_posiciones_por_ronda(resultados_ronda, ronda_actual, tema):
    """
     Esta función ordena las posiciones y las imprime las posiciones de cada ronda
    """
    posiciones_ordenadas = sorted(resultados_ronda, key=lambda x: x[1], reverse=True)
    print(f"Ronda {ronda_actual} - {tema}:")
    print()
    print("Posiciones:")
    for (nombre,puntos) in posiciones_ordenadas:
        print(f"{nombre:<15} {puntos:<20}")
    print()
    

#------------------------------SIMULACIÓN DE COMPETENCIA----------------------------#
def simular_competencia(rounds):
    """
     Esta función simula la competencia de cocina procesando cada ronda de la lista 'rounds', genera las estadísticas para todos los cocineros (competidores) y se actualiza en cada ronda
    """

    #De la ronda 0, se obtiene el nombre de los cocineros (las 'keys' del diccionario) y se guardan en la variable cocineros
    nombre_cocinero = rounds[0]['scores'].keys()
    #Se define un diccionario por comprensión a partir de cocineros
    estadisticas = {cocinero: {'total_puntos': 0, 'rondas_ganadas': 0, 'mejor_ronda': 0} for cocinero in nombre_cocinero}

    cant_rondas = len(rounds)
    ronda_actual = 1

    #Se procesa cada ronda
    for ronda in rounds:

        scores_ronda = ronda['scores']
        tema = ronda['theme']
    
        # Se procesa el puntaje (Con la forma {'Valentina': {'judge_1': 8, 'judge_2': 7,'judge_3': 9}') 

        resultados_ronda = list(map(lambda item: (item[0], sumar_puntajes_jueces(item[1])), scores_ronda.items()))
        ganador = max(resultados_ronda, key=lambda x: x[1])
        nombre_ganador = ganador[0]
        puntos_ganador = ganador[1]

        #Se imprime imprime la tabla de posiciones de cada ronda
        imprimir_posiciones_por_ronda(resultados_ronda, ronda_actual, tema)

        #Se actualizan las estadísticas del ganador
        estadisticas[nombre_ganador]['rondas_ganadas'] += 1

        #Este bloque imprime la victoria
        print(f"Ronda {ronda_actual} - {tema}:")
        print(f"  Ganador: {nombre_ganador} ({puntos_ganador} pts)")
        print()

        #Este bloque actualiza las estadisticas de cada cocinero
        for (nombre, puntos) in resultados_ronda:

            estadisticas[nombre]['total_puntos'] += puntos

            if puntos > estadisticas[nombre]['mejor_ronda']:
                estadisticas[nombre]['mejor_ronda'] = puntos

        ronda_actual += 1
        print()
    generar_tabla_posiciones(estadisticas,cant_rondas)



