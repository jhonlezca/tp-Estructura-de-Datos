# Para la primer estrategia, vamos a usar la funcion que ya tenemos definida en el archivo Liga.py, la cual realiza una búsqueda lineal dentro de todos los equipos de la liga, y nos devuelve el equipo que coincide con el nombre que le pasamos como parámetro. 
import json
from Equipo import Equipo
import time

with open("tp-Estructura-de-Datos\\equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

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

# Para la segunda, vamos a utilizar una búsqueda binaria. Como el elemento que usamos para buscar es el nombre, en primer lugar tendríamos que tener la lista ordenada de manera ascendente. 

def buscarEquipoPorNombre_binaria(lista_equipos, nombre_equipo):
        nombre_buscar = nombre_equipo.strip().lower()
        equipos_ordenados = sorted(lista_equipos, key=lambda equipo: equipo["nombre"].lower())
        inicio = 0
        fin = len(equipos_ordenados) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            equipo_actual = equipos_ordenados[medio]

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

equipos = fabricaDeEquipos(1000)  # Llamada a la función para crear n equipos

# Ejemplo de uso : Busqueda Lineal
datos_equipos = equipos
nombre_1 = input("Ingrese equipo: ")
inicio = time.perf_counter()
buscarEquipoPorNombre_lineal(datos_equipos, nombre_1)
fin = time.perf_counter()
tiempo_transcurrido = fin - inicio
print(f"Tiempo de ejecucion: {tiempo_transcurrido:.8f} segundos")

# Ejemplo de uso : Busqueda Binaria

# datos_equipos = datos["equipos"]
# nombre_1 = input("Ingrese equipo: ")
# inicio = time.perf_counter()
# buscarEquipoPorNombre_binaria(datos_equipos, nombre_1)
# fin = time.perf_counter()
# tiempo_transcurrido = fin - inicio
# print(f"Tiempo de ejecucion: {tiempo_transcurrido:.8f} segundos")

