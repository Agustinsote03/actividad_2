def simular_competencia(rounds):
    """
     simulacion
    """

    #Se obtiene el nombre de los cocineros (las 'keys' del diccionario) y se guardan en la variable cocineros
    nombre_cocinero = rounds['scores'].keys()

    #Se define un diccionario por comprensión a partir de cocineros
    estadisticas = {nombre_cocinero: {'total_puntos': 0, 'rondas_ganadas': 0, 'mejor_ronda': 0} for cocinero in nombre_cocinero}

    cant_rondas = len(rounds)
    ronda_actual = 1

    #Se procesa cada ronda
    for ronda in rounds:

        scores_ronda = ronda['scores']
        tema = ronda['theme']
        
        resultados_ronda = 



