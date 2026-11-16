import json
import TP05
from Liga import Liga
import TP07
import TP08

with open("equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

equiposArgentinos = datos["equipos"]
liga_argentina = Liga("Liga Argentina", equiposArgentinos, len(equiposArgentinos))

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
        print("5. Buscar jugadores (grafos de similitud)")
        print("6. Consultar jugadores cercanos por edad (BFS) y misma posición (DFS)")
        print("7. Salir")
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
            Liga.menu_filtrar_por_grafo(liga_argentina)

        elif opcion == "6":
            print("\n--- CONSULTA DE JUGADORES ---")
            print("1. Buscar jugadores cercanos por edad (BFS)")
            print("2. Buscar jugadores con la misma posición (DFS)")

            sub_opcion = input("\nSeleccioná una opción: ").strip()

            if sub_opcion == "1":
                Liga.menu_consultar_cercanos(liga_argentina)
            elif sub_opcion == "2":
                Liga.menu_consultar_misma_posicion(liga_argentina)
            else:
                print("⚠️ Opción inválida. Intentá de nuevo.")
        
        elif opcion == "7":
            print("¡Gracias por usar Futbolero! ¡Hasta la próxima!")
            break
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()