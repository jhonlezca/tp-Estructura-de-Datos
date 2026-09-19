class Jugador:
    def __init__(self, id_jugador, nombre, apellido, dorsal, posicion, nacionalidad):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.apellido = apellido
        self.dorsal = dorsal
        self.posicion = posicion
        self.nacionalidad = nacionalidad



    def __str__(self):
        return f" \n NOMBRE : {self.nombre} \n APELLIDO : {self.apellido} \n Dorsal: {self.dorsal}\n Posición: {self.posicion}\n Nacionalidad: {self.nacionalidad} \n"
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}".strip()
    
    def __repr__(self):
        return f"Jugador(id={self._id_jugador!r}, nombre={self._nombre!r}, dorsal={self._dorsal!r})"
    
