import json
from Equipo import Equipo
from TP03 import ArbolBinarioBusqueda 
from TP06 import Heap
import TP07
import TP08
import random


with open("equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

equiposArgentinos = datos["equipos"]

jugadores = []


class Liga:
    def __init__(self, nombre, equipos, cantidad_equipos):
        self.nombre = nombre
        self.equipos = equipos
        self.cantidad_equipos = cantidad_equipos
        self.arbol_equipos = ArbolBinarioBusqueda()
        self.tabla_de_posiciones = Heap()
        # Poblamos el arbol desordenando previamente la lista para que las ramificaciones tengan sentido
        
        if self.equipos:
            self.poblar_arbol_desordenado()

    def poblar_arbol_desordenado(self):
        # hacemos una copia para desordenar sin alterar la lista original
        copia_desordenada = self.equipos.copy()
        random.shuffle(copia_desordenada)
        
        for equipo in copia_desordenada:
            self.arbol_equipos.insertar(equipo)
        
    # Es la funcion original de Agregar Equipo pero ahora tambien inserta el equipo al arbol
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
        self.arbol_equipos.insertar(equipo)

    # Se encarga de buscar un equipo por su nombre y mostrar información del mismo

    def buscarEquipoPorNombre(self, nombre_equipo):
        nombre_buscar = nombre_equipo.strip().lower()
        
        for equipo in self.equipos:
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
                equipoConsultado.mostrar_Plantel() # agregue la parte de mostrar el plantel (no la tenia)
                return  # <--- RETORNA Y SALE si lo encuentra

        # Si recorrió todo el for y no lo encontró:
        print(f"\n❌ No se encontró el equipo '{nombre_equipo}'.")
    
    def listarEquipos(self):
        """Retorna la lista de equipos registrados en la liga"""
        return self.equipos
    
    def buscarEquipoPorNombreArbol(self, nombre_equipo):
        return self.arbol_equipos.buscar(nombre_equipo)
    
    def listarEquiposArbol(self):
        return self.arbol_equipos.recorrido_inorder()
    
    # recibe una lista de  tuplas de  equipos con su posicion en el campeonato  y los inserta en la tabla de posiciones
    def posiciones(self):
        tabla = []
        for posicion, equipo in enumerate(self.equipos, start=1):
            tabla.append(( equipo["nombre"], posicion))
        return tabla
        
    def cargar_tabla_de_posiciones(self, tabla):
        
        for equipo_pos in tabla:
            self.tabla_de_posiciones.insertar(equipo_pos)

    def topN_equipos(self, n):
        """Retorna una lista con los n equipos mejor posicionados en la tabla de posiciones"""
        for equipo in self.tabla_de_posiciones.obtener_n_mas_pequenos(n):
            print(f" Posición: {equipo[1]} --->  {equipo[0]}")

    def listar_jugadores(self):
        for linea in jugadores:
            print(f"Nombre: {linea['nombre']} {linea['apellido']}, Nacionalidad: {linea['nacionalidad']}, Posición: {linea['posicion']}")
        return f"Total de jugadores: {len(jugadores)}"

    def obtener_todos_los_jugadores(self):
        """Devuelve una lista de todos los jugadores de la liga"""
        todos = []
        for equipo in self.equipos:
            plantel = equipo.get("plantel", [])
            todos.extend(plantel)
        return todos
    
    def menu_consultar_cercanos(liga_argentina):
        todos = liga_argentina.obtener_todos_los_jugadores()
        grafo = TP08.GrafoJugadores()

        print("\n==============================================")
        print("   BÚSQUEDA DE JUGADORES CERCANOS POR EDAD (BFS)")
        print("==============================================")
        
        busqueda = input("Ingresá el nombre o apellido del jugador (ej. Cavani): ").strip()
        max_niveles_str = input("Ingresá la cantidad máxima de niveles de cercanía (ej. 1, 2): ").strip()

        try:
            max_niveles = int(max_niveles_str)
        except ValueError:
            print("⚠️ Se usará el valor por defecto: 2 niveles.")
            max_niveles = 2

        # 1. Construir el grafo conectando edades con hasta 1 año de diferencia
        grafo.construir_red_cercania_edad(todos, salto_maximo=1)

        # 2. Ejecutar recorrido BFS
        jugador_encontrado, resultados = grafo.buscar_cercanos_edad_bfs(busqueda, max_niveles)

        if not jugador_encontrado:
            print(f"\n❌ No se encontró ningún jugador que coincida con '{busqueda}' en la base de datos.")
            return

        ref = grafo.jugadores_map[jugador_encontrado]
        edad_ref = ref.get('edad') if isinstance(ref, dict) else ref.edad

        print(f"\n==================================================")
        print(f" RED BFS DESDE: {jugador_encontrado} ({edad_ref} años)")
        print(f"==================================================")

        if resultados:
            for nivel, jugadores in sorted(resultados.items()):
                print(f"\n• Nivel {nivel} (a {nivel} salto/s de edad):")
                for jug in jugadores:
                    if isinstance(jug, dict):
                        nombre = f"{jug.get('nombre')} {jug.get('apellido')}"
                        edad = jug.get('edad', 'S/D')
                    else:
                        nombre = jug.nombre_completo
                        edad = jug.edad
                    print(f"   └── {nombre} ({edad} años)")
        else:
            print(f"\nℹ️ {jugador_encontrado} no tiene jugadores conectados dentro de {max_niveles} niveles.")

    def menu_filtrar_por_grafo(liga_argentina):
        
        # 1. Obtener la lista acumulada de jugadores
        todos = liga_argentina.obtener_todos_los_jugadores()
        grafo = TP07.GrafoFiltroAtributo()

        print("\n==============================================")
        print("   BÚSQUEDA Y FILTRADO POR GRAFO DE SIMILITUD")
        print("==============================================")
        print("1. Filtrar por Nacionalidad")
        print("2. Filtrar por Posición")
        print("3. Filtrar por Edad")

        opcion = input("\nSeleccioná el atributo a filtrar (1-3): ").strip()

        atributo = None
        if opcion == "1":
            atributo = "nacionalidad"
            valor = input("Ingresá la nacionalidad deseada (ej. Argentina, Uruguaya): ")
        elif opcion == "2":
            atributo = "posicion"
            valor = input("Ingresá la posición deseada (ej. Delantero, Mediocampista): ")
        elif opcion == "3":
            atributo = "edad"
            valor = input("Ingresá la edad deseada (ej. 25, 30): ")
        
        # 2. Construir el subgrafo con las elecciones del usuario
        grafo.construir_subgrafo_por_atributo(todos, atributo, valor)

        # 3. Consultar y mostrar los resultados generados en la red
        red = grafo.obtener_red_filtrada()

        if red:
            print(f"\n==================================================")
            print(f" RED DE JUGADORES FILTRADOS POR {atributo.upper()}: '{valor}'")
            print(f" Total de Nodos Conectados: {len(red)}")
            print(f"==================================================")
            
            for jug, conexiones in red:
                if isinstance(jug, dict):
                    nombre = f"{jug.get('nombre')} {jug.get('apellido')}"
                    pos = jug.get('posicion', 'S/D')
                    nac = jug.get('nacionalidad', 'S/D')
                else:
                    nombre = jug.nombre_completo
                    pos = jug.posicion
                    nac = jug.nacionalidad

                print(f"• {nombre} ({pos} - {nac})")
                print(f"   └── Conectado con otros {conexiones} jugadores del grupo.")
        else:
            print(f"\n❌ No se encontraron jugadores con {atributo} = '{valor}'.")
            
    def menu_consultar_misma_posicion(liga_argentina):
        todos = liga_argentina.obtener_todos_los_jugadores()
        grafo = TP08.GrafoJugadores()

        print("\n==============================================")
        print("   EXPLORACIÓN DE POSICIÓN EN PROFUNDIDAD (DFS)")
        print("==============================================")
        
        busqueda = input("Ingresá el nombre o apellido del jugador referencia: ").strip()

        # 1. Construir la red por posición
        grafo.construir_red_posicion(todos)

        # 2. Ejecutar recorrido DFS
        jugador_encontrado, resultados = grafo.explorar_posicion_dfs(busqueda)

        if not jugador_encontrado:
            print(f"\n❌ No se encontró ningún jugador que coincida con '{busqueda}' en la base de datos.")
            return

        ref = grafo.jugadores_map[jugador_encontrado]
        pos_ref = ref.get('posicion') if isinstance(ref, dict) else ref.posicion

        print(f"\n==================================================")
        print(f" RED DFS DESDE: {jugador_encontrado} (Posición: {pos_ref})")
        print(f" Total de jugadores alcanzados en la rama: {len(resultados)}")
        print(f"==================================================")

        for jug in resultados:
            if isinstance(jug, dict):
                nombre = f"{jug.get('nombre')} {jug.get('apellido')}"
                pos = jug.get('posicion', 'S/D')
            else:
                nombre = jug.nombre_completo
                pos = jug.posicion
            print(f"• {nombre} ({pos})")

#liga = Liga("Liga Argentina", equiposArgentinos, len(equiposArgentinos))


#liga.cargar_tabla_de_posiciones(liga.posiciones())


#print   ("Top 5 equipos mejor posicionados en la tabla de posiciones:")

#print(liga.topN_equipos(5))
