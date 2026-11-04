import json
import TP05
from Liga import Liga
import TP07

with open("equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

equiposArgentinos = datos["equipos"]
liga_argentina = Liga("Liga Argentina", equiposArgentinos, len(equiposArgentinos))

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
    else:
        print("⚠️ Opción no válida.")
        return

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

def main():
    print("="*24)
    print(" BIENVENIDO A FUTBOLERO ")
    print("="*24)
    print(" Ahora, ademas de nuestras funciones clasicas, tambien podes utilizar las nuevas desarrolladas con Arbol de Busqueda Binaria (ABB). ¡Probalas!")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar equipo por nombre")
        print("2. Listar todos los equipos")
        print("3. Buscar equipo por nombre (ABB)")
        print("4. Listar todos los equipos (ABB)")
        print("5. Buscar jugadores")
        print("6. Salir")
        print("\n(Consejo: Utiliza primero la opcion 2 para conocer los nombres de los equipos registrados)\n")
        
        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            nombre = input("\nIngresá el nombre de tu equipo favorito: ")
            liga_argentina.buscarEquipoPorNombre(nombre)

        elif opcion == "2":
            print("\n--- EQUIPOS REGISTRADOS ---")
            for eq in liga_argentina.listarEquipos():
                print(f"• {eq['nombre']}")

        elif opcion == "3":
            nombre = input("\nIngresá el nombre del equipo a buscar: ")
            equipo_hallado = liga_argentina.buscarEquipoPorNombre(nombre)

            if equipo_hallado:
                print(f"\n¡Encontrado!: {equipo_hallado.nombre}")
                print(f"Estadio: {equipo_hallado.estadio}")
            else:
                print("❌ Equipo no encontrado en el árbol.")
        
        elif opcion == "4":
            print("\n--- EQUIPOS EN ORDEN ALFABÉTICO (Recorrido Inorder) ---")
            for eq in liga_argentina.listarEquipos():
                print(f"• {eq['nombre']}")

        elif opcion == "5":
            menu_filtrar_por_grafo(liga_argentina)

        elif opcion == "6":
            print("\nSaliendo. Gracias por utilizar Futbolero ;) \n")
            break
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()