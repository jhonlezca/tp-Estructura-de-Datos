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
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar equipo por nombre")
        print("2. Listar todos los equipos")
        print("3. Buscar equipos (ABB)")
        print("4. Tabla de posiciones (heap)")
        print("5. Filtrar jugadores (grafos de similitud)")
        print("6. Consultar jugadores cercanos por edad (BFS) y misma posición (DFS)")
        print("7. Consultar jugadores por nacionalidad (Árbol N-ario)")
        print("8. Salir")
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
            liga_argentina.menu_arbol_abb()

        elif opcion == "4":
            liga_argentina.menu_posiciones()
        
        elif opcion == "5":
            liga_argentina.menu_filtrar_jugadores()

        elif opcion == "6":
            liga_argentina.menu_jugadores_cercanos()
            
        elif opcion == "7":
            liga_argentina.menu_arbol_nacionalidades()
            
        elif opcion == "8":
            print("\n--- SALIR ---")
            print("¡Gracias por usar Futbolero! ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()