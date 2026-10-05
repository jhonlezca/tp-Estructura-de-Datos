import json

from Liga import Liga

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
        print("5. Salir")
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

            print("\nGracias por utilizar Futbolero ;) \n")
            break
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()