import json
from Equipo import Equipo 


with open("tp-Estructura-de-Datos/equipos_argentina.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

equiposArgentinos = datos["equipos"]

class Liga:
    def __init__(self, nombre, equipos, cantidad_equipos):
        self.nombre = nombre
        self.equipos = equipos
        self.cantidad_equipos = cantidad_equipos
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

# Se encarga de buscar un equipo por su nombre y mostrar información del mismo

    def buscarEquipoPorNombre(self, nombre_equipo):
        for equipo in self.equipos:
            if equipo["nombre"].lower() == nombre_equipo.lower():

                equipoConsultado = Equipo(equipo["id"], equipo["nombre"], equipo["estadio"], equipo.get("zona"), equipo.get("pos_campeonato"), equipo.get("partidos"), equipo.get("plantel"))
                equipoConsultado.mostrar_Informacion()
                equipoConsultado.filtrarJugadoresPorNacionalidad("argentina")
                break

 



        

liga_argentina = Liga("Liga Argentina", equiposArgentinos, len(equiposArgentinos))

liga_argentina.buscarEquipoPorNombre("club Atlético AldoSIVI")

