#------------------------------FUNCIONES AUXILIARES----------------------------#
def sumar_puntajes_jueces(puntaje_jueces):
    """
     Esta función toma el diccionario con las puntuaciones de los jueces y retorna la suma de ellos
    """
    total_puntos = sum(puntaje_jueces.values())
    return total_puntos

def generar_tabla_posiciones(estadisticas):
    pass
#------------------------------SIMULACIÓN DE COMPETENCIA----------------------------#
def simular_competencia(rounds):
    """
     simulacion
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

        #Se actualizan las estadísticas del ganador
        estadisticas[nombre_ganador]['rondas_ganadas'] += 1

        #Este bloque imprime la victoria
        print(f"Ronda {ronda} - {tema}:")
        print(f"  Ganador: {nombre_ganador} ({puntos_ganador} pts)")
        print()

        #Este bloque actualiza las estadisticas de cada cocinero
        for nombre, puntos in resultados_ronda:

            estadisticas[nombre]['total_puntos'] += puntos

            if puntos > estadisticas[nombre]['mejor_ronda']:
                estadisticas[nombre]['mejor_ronda'] = puntos
        print()
        generar_tabla_posiciones(estadisticas)



