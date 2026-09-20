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
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar equipo por nombre")
        print("2. Listar todos los equipos")
        print("3. Salir")
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
            print("\nGracias por utilizar Futbolero ;) \n")
            break
        else:
            print("⚠️ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()