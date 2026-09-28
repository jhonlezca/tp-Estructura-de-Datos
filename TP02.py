# Para la primer estrategia, vamos a usar la funcion que ya tenemos definida en el archivo Liga.py, la cual realiza una búsqueda lineal dentro de todos los equipos de la liga, y nos devuelve el equipo que coincide con el nombre que le pasamos como parámetro. 

from Equipo import Equipo
import time

def buscarEquipoPorNombre_lineal(lista_equipos, nombre_equipo):
        nombre_buscar = nombre_equipo.strip().lower()
        
        for equipo in lista_equipos:
            if equipo["nombre"].lower() == nombre_buscar:
                equipoConsultado = Equipo(
                    equipo["id"], 
                    equipo["nombre"], 
                    equipo["estadio"], 
                    equipo.get("zona"), 
                    equipo.get("pos_campeonato"), 
                    equipo.get("partidos"), 
                    equipo.get("plantel")
                )
                print("\nDatos del equipo:")
                equipoConsultado.mostrar_Informacion()
                equipoConsultado.mostrar_Plantel() 
                return  # <--- RETORNA Y SALE si lo encuentra

        # Si recorrió todo el for y no lo encontró:
        print(f"\n❌ No se encontró el equipo '{nombre_equipo}'.")

# Para la segunda, vamos a utilizar una búsqueda binaria. Vale aclarar que, como el elemento que usamos para buscar es el nombre, debemos tener la lista ordenada de manera ascendente.

def buscarEquipoPorNombre_binaria(lista_equipos, nombre_equipo):
        nombre_buscar = nombre_equipo.strip().lower()
        inicio = 0
        fin = len(lista_equipos) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            equipo_actual = lista_equipos[medio]

            if equipo_actual["nombre"].lower() == nombre_buscar:
                equipoConsultado = Equipo(
                    equipo_actual["id"], 
                    equipo_actual["nombre"], 
                    equipo_actual["estadio"], 
                    equipo_actual.get("zona"), 
                    equipo_actual.get("pos_campeonato"), 
                    equipo_actual.get("partidos"), 
                    equipo_actual.get("plantel")
                )
                print("\nDatos del equipo:")
                equipoConsultado.mostrar_Informacion()
                equipoConsultado.mostrar_Plantel() # agregue la parte de mostrar el plantel (no la tenia)
                return  # <--- RETORNA Y SALE si lo encuentra

            elif nombre_buscar < equipo_actual["nombre"].lower():
                fin = medio - 1
            else:
                inicio = medio + 1

        # Si salió del while sin encontrar el equipo:
        print(f"\n❌ No se encontró el equipo '{nombre_equipo}'.")

def fabricaDeEquipos(cantidadEquipos):
    equipos = []
    id = 0
    while id <= cantidadEquipos:
        equipo_obj = { "id": id, "nombre": f"Equipo{id}", "estadio": "", "zona": "", "pos_campeonato": {}, "partidos": {}, "plantel": [] }
        id += 1
        equipos.append(equipo_obj)          
    return equipos 

tamaño = [100, 1000, 10000, 100000, 500000]
equipo_inexistente = "Equipo_9999_ZZZZ"
contador = 1

for i in tamaño:
    equipos = fabricaDeEquipos(i)
    
    # Medicion busqueda binaria
    
    equipos_ordenados = sorted(equipos, key=lambda equipo: equipo["nombre"].lower()) # Ordenamos la lista de manera ascendente
    print(f"Busqueda binaria {contador}")
    inicio_binaria = time.perf_counter()
    buscarEquipoPorNombre_binaria(equipos, equipo_inexistente)
    fin_binaria = time.perf_counter()
    tiempo_transcurrido_binaria = fin_binaria - inicio_binaria
    print(f"Tiempo de ejecucion de busqueda binaria con {i} equipos: {tiempo_transcurrido_binaria:.8f}")
    
    # Medicion busqueda lineal 
    
    print(f"Busqueda lineal {contador}")
    inicio_lineal = time.perf_counter()
    buscarEquipoPorNombre_lineal(equipos, equipo_inexistente)
    fin_lineal = time.perf_counter()
    tiempo_transcurrido_lineal = fin_lineal - inicio_lineal
    print(f"Tiempo de ejecucion de busqueda lineal con {i} equipos: {tiempo_transcurrido_lineal:.8f}")
    contador = contador + 1

# REGISTRO DE TIEMPOS DE EJECUCION: 

# busqueda binaria con 100 equipos:     0.00014700
# busqueda lineal con 100 equipos:      0.00015790

# busqueda binaria con 1000 equipos:    0.00006520
# busqueda lineal con 1000 equipos:     0.00021760

# busqueda binaria con 10000 equipos:   0.00015480
# busqueda lineal con 10000 equipos:    0.00086770

# busqueda binaria con 100000 equipos:  0.00011100
# busqueda lineal con 100000 equipos:   0.01081180

# busqueda binaria con 500000 equipos: 0.00009840
# busqueda lineal con 500000 equipos: 0.04029510

# ANALISIS Y CONCLUSIONES

# Busqueda lineal

#  En este caso, estamos recorriendo la lista elemento por elemento de forma secuencial. A partir de ello, determinamos los siguientes tres casos:
#     Peor caso - O(N): ocurre cuando el equipo buscado no existe en la lista o se encuentra en la ultima posicion. El algoritmo realiza N comparaciones.
#     Mejor caso - Ω(1): ocurre cuando el equipo buscado esta justo en la primer posicion, realizando una sola comparacion.
#     Caso promedio - Θ(N): en promedio el algoritmo va a realizar N / 2 comparaciones, manteniendo un comportamiento lineal respecto a N.

# Busqueda Binaria

#  Suponiendo que la lista ya se encuentra previamente ordenada, determinamos los siguientes casos:
#   Peor caso - O(log N): en cada while, el algoritmo descarta la mitad de los elementos. En el peor caso, el elemento no existe o esta en un extremo; realizandose (como mucho) log en base 2 (N) comparaciones. 
#   Mejor caso - Ω(1): Ocurre cuando el elemento buscado coincide con la mitad de la lista.
#   Caso Promedio — Θ(log N): En promedio, descartar la mitad en cada paso requiere aproximadamente log en base 2 (N) - 1 iteraciones.

#   CONCLUSION
#  Considerando que la búsqueda lineal depende de qué tan pronto se encuentre el equipo en la lista, determinamos que para nuestro programa utilizar búsqueda binaria resulta más efectivo. Con ella, se logra un promedio general mucho más bajo que con la lineal; además, el peor de los casos es menos "peor" que con el primer algoritmo de búsqueda.