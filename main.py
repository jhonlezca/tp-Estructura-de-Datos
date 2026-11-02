import json
import TP05
from Liga import Liga
import TP07

with open("equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

equiposArgentinos = datos["equipos"]
liga_argentina = Liga("Liga Argentina", equiposArgentinos, len(equiposArgentinos))

def menu_jugadores():
    print("1. Buscar por nacionalidad. ")
    print("2. Buscar por edad. ")
    opcion = input("Ingrese una opcion: ").strip()
    if opcion == "1":
        nacionalidad = input("Ingrese una nacionalidad: ")
        nacionalidades = TP05.ArbolNacionalidades()
        return nacionalidades.listar_jugadores_por_nacionalidad(nacionalidad)
    elif opcion == "2":
        print("1. Busqueda por rango de edad")
        print("2. Busqueda por edad similar")
        subopcion = input("Ingrese una opcion: ")
        if subopcion == "1":
            TP07.GrafoEdades.buscar_por_rango_edad()
        elif subopcion == "2":
            TP07.GrafoEdades.obtener_jugadores_de_edad_similar()
        else:
            print("Ingrese opcion correcta.")
    else:
        print("Ingrese opcion correcta. ")

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
            menu_jugadores
            
        elif opcion == "6":
            print("\nSaliendo. Gracias por utilizar Futbolero ;) \n")
            break
        
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()