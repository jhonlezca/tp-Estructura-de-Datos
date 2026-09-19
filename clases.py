import json


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


    def buscarEquipoPorNombre(self, nombre_equipo):
        for equipo in self.equipos:
            if equipo["nombre"].lower() == nombre_equipo.lower():

                equipoConsultado = Equipo(equipo["id"], equipo["nombre"], equipo["estadio"], equipo.get("zona"), equipo.get("pos_campeonato"), equipo.get("partidos"), equipo.get("plantel"))
                equipoConsultado.mostrar_Informacion()
                equipoConsultado.mostrar_Plantel()
                break
              
            else:
                print(f"No se encontró el equipo con el nombre '{nombre_equipo}'.")
                
     



    
class Jugador:
    def __init__(self, id_jugador, id_equipo, nombre, apellido, dorsal, posicion):
        self.id_jugador = id_jugador
        self.id_equipo = id_equipo
        self.nombre = nombre
        self.apellido = apellido
        self.dorsal = dorsal
        self.posicion = posicion
    
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}".strip()
    
    @property
    def dorsal(self):
        return self._dorsal
    
    @property
    def posicion(self):
        return self._posicion
    
    def __str__(self):
        return f"{self.dorsal}, {self.nombre} {self.apellido}, {self.posicion}"
    
    def __repr__(self):
        return f"Jugador(id={self._id_jugador!r}, nombre={self._nombre!r}, dorsal={self._dorsal!r})"
    
    
class Equipo:
    def __init__(self, id_equipo, nombre, estadio, zona=None, pos_campeonato=None, partidos=None, plantel=None):
        self._id = id_equipo
        self._nombre = nombre
        self._estadio = estadio
        self._zona = zona
        self._pos_campeonato = pos_campeonato or {}
        self._partidos = partidos or {}
        self._plantel = plantel or   []

    def mostrar_Informacion(self):
        print(f"ID: {self._id}")
        print(f"Nombre: {self._nombre}")
        print(f"Estadio: {self._estadio}")
        print(f"Zona: {self._zona}") 

    def mostrar_Plantel(self):
        if self._plantel:
            print(f"Plantel del equipo {self._nombre}:")
            for jugador in self._plantel:
                print(f"- {jugador['nombre']} {jugador['apellido']}, Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']}")
        else:
            print(f"No hay jugadores registrados en el plantel del equipo {self._nombre}.")
  
  
       
        
    @property
    def id(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def estadio(self):
        return self._estadio
    @property
    def zona(self):
        return self._zona
    @property
    def partidos(self):
        return self._partidos
    @property
    def plantel(self):
        return self._plantel
    
    
    def __repr__(self):
        return f"Equipo (id={self._id!r})"


# Prueba de la clase Liga y la búsqueda de un equipo por nombre
liga_argentina = Liga("Liga Argentina", equiposArgentinos, len(equiposArgentinos))

liga_argentina.buscarEquipoPorNombre("club Atlético AldoSIVI")