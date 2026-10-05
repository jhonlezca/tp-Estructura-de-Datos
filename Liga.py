import json
from Equipo import Equipo
from TP03 import ArbolBinarioBusqueda 
import random


with open("equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

equiposArgentinos = datos["equipos"]

class Liga:
    def __init__(self, nombre, equipos, cantidad_equipos):
        self.nombre = nombre
        self.equipos = equipos
        self.cantidad_equipos = cantidad_equipos
        self.arbol_equipos = ArbolBinarioBusqueda()
        
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
    