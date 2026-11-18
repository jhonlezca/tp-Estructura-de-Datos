import json
from Equipo import Equipo
from TP03 import ArbolBinarioBusqueda
from TP04 import ArbolAVL
import TP05
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
        self.arbol_avl_equipos = ArbolAVL()
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
    
    def posiciones_zona_A(self):
        """Devuelve una lista de tuplas (equipo, posicion) para la zona A"""
        tabla = []
        for equipo in self.equipos:
            if equipo.get("zona") == "A":
                pos = equipo.get("campeonato", {}).get("posicion")
                tabla.append((equipo["nombre"], pos))
        return tabla
        
    def posiciones_zona_B(self):
        """Devuelve una lista de tuplas (equipo, posicion) para la zona B"""
        tabla = []
        for equipo in self.equipos:
            if equipo.get("zona") == "B":
                pos = equipo.get("campeonato", {}).get("posicion")
                tabla.append((equipo["nombre"], pos))
        return tabla
    
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
    
    def buscar_por_nombre_arbol_avl(self, nombre_equipo):
        """Busca un equipo por nombre en el árbol AVL."""
        return self.arbol_avl_equipos.buscar(nombre_equipo)
    
    def listar_equipos_arbol_avl(self):
        """Devuelve una lista de equipos ordenados alfabéticamente usando el recorrido Inorder del árbol AVL."""
        return self.arbol_avl_equipos.recorrido_inorder()

    def menu_arbol_avl(self):
        print("\n--- MENÚ DE ÁRBOL AVL ---")
        print("1. Buscar equipo por nombre (AVL)")
        print("2. Listar todos los equipos (AVL)")
        print("3. Salir del menú AVL")
        
        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            nombre = input("\nIngresá el nombre del equipo a buscar: ")
            equipo_hallado = self.buscar_por_nombre_arbol_avl(nombre)

            if equipo_hallado:
                print(f"\n¡Encontrado!: {equipo_hallado.nombre}")
                print(f"Estadio: {equipo_hallado.estadio}")
            else:
                print("❌ Equipo no encontrado en el árbol AVL.")
        
        elif opcion == "2":
            print("\n--- EQUIPOS EN ORDEN ALFABÉTICO (Recorrido Inorder AVL) ---")
            for eq in self.listar_equipos_arbol_avl():
                print(f"• {eq['nombre']}")
        
        elif opcion == "3":
            print("Saliendo del menú AVL...")
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")
    
    def menu_arbol_abb(self):
        print("\n--- MENÚ DE ÁRBOL ABB ---")
        print("1. Buscar equipo por nombre (ABB)")
        print("2. Listar todos los equipos (ABB)")
        print("3. Salir del menú ABB")
        
        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            nombre = input("\nIngresá el nombre del equipo a buscar: ")
            equipo_hallado = self.buscarEquipoPorNombreArbol(nombre)

            if equipo_hallado:
                print(f"\n¡Encontrado!: {equipo_hallado.nombre}")
                print(f"Estadio: {equipo_hallado.estadio}")
            else:
                print("❌ Equipo no encontrado en el árbol ABB.")
        
        elif opcion == "2":
            print("\n--- EQUIPOS EN ORDEN ALFABÉTICO (Recorrido Inorder ABB) ---")
            for eq in self.listarEquiposArbol():
                print(f"• {eq['nombre']}")
        
        elif opcion == "3":
            print("Saliendo del menú ABB...")
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")
    
    def nacionalidades(self):
        """Crea un árbol de nacionalidades y devuelve el objeto del árbol"""
        arbol_nacionalidades = TP05.ArbolNacionalidades()
        arbol_nacionalidades.cargar_jugadores_desde_equipos(self.equipos)
        return arbol_nacionalidades
    
    def buscar_por_nacionalidad(self, nacionalidad):
        """Busca jugadores por nacionalidad usando el árbol de nacionalidades"""
        arbol_nacionalidades = self.nacionalidades()
        jugadores_encontrados = arbol_nacionalidades.buscar_jugador_por_nacion(nacionalidad)
        
        if jugadores_encontrados:
            print(f"\n=== JUGADORES DE {nacionalidad.upper()} ({len(jugadores_encontrados)}) ===")
            for jugador in jugadores_encontrados:
                print(jugador)
        else:
            print(f"\n❌ No se encontraron jugadores con nacionalidad '{nacionalidad}'.")
    
    def heap_posiciones_zona_A(self):
        """Crea un heap con los equipos de la zona A y sus posiciones"""
        tabla = self.posiciones_zona_A()
        for equipo_pos in tabla:
            self.tabla_de_posiciones.insertar(equipo_pos)
    
    def heap_posiciones_zona_B(self):
        """Crea un heap con los equipos de la zona B y sus posiciones"""
        tabla = self.posiciones_zona_B()
        for equipo_pos in tabla:
            self.tabla_de_posiciones.insertar(equipo_pos)
    
    def menu_posiciones(self):
        print("\n--- MENÚ DE TABLA DE POSICIONES (Heap) ---")
        print("1. Mostrar top 3 equipos mejor posicionados (zona A)")
        print("2. Mostrar top 3 equipos mejor posicionados (zona B)")
        print("3. Salir del menú de posiciones")

        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            self.heap_posiciones_zona_A()
            print("\n--- TOP 3 EQUIPOS MEJOR POSICIONADOS (ZONA A) ---")
            for equipo, pos in self.tabla_de_posiciones.obtener_n_mas_pequenos(3):
                print(f"Posición {pos}: {equipo}")
        
        elif opcion == "2":
            self.heap_posiciones_zona_B()
            print("\n--- TOP 3 EQUIPOS MEJOR POSICIONADOS (ZONA B) ---")
            for equipo, pos in self.tabla_de_posiciones.obtener_n_mas_pequenos(3):
                print(f"Posición {pos}: {equipo}")
        
        elif opcion == "3":
            print("Saliendo del menú de posiciones...")
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

    def menu_arbol_nacionalidades(self):
        print("\n--- MENÚ DE ÁRBOL N-ARIO DE NACIONALIDADES ---")
        print("1. Consultar jugadores por nacionalidad")
        print("2. Salir del menú de nacionalidades")
        
        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            nacionalidad = input("\nIngresá la nacionalidad a buscar: ").strip()
            self.buscar_por_nacionalidad(nacionalidad)
        
        elif opcion == "2":
            print("Saliendo del menú de nacionalidades...")
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

#liga.cargar_tabla_de_posiciones(liga.posiciones())


#print   ("Top 5 equipos mejor posicionados en la tabla de posiciones:")

#print(liga.topN_equipos(5))
