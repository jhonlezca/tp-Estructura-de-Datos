class Jugador:
    def __init__(self, id_jugador, nombre, apellido, dorsal, posicion, nacionalidad, edad=None):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.apellido = apellido
        self.dorsal = dorsal
        self.posicion = posicion
        self.nacionalidad = nacionalidad
        self.edad = edad  # Asignamos la edad directamente si es proporcionada



    def __str__(self):
        return f" \n NOMBRE : {self.nombre} \n APELLIDO : {self.apellido} \n Dorsal: {self.dorsal}\n Posición: {self.posicion}\n Nacionalidad: {self.nacionalidad} \n Edad: {self.edad if self.edad is not None else 'No disponible'}\n"
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}".strip()
    
    def __repr__(self):
        return f"Jugador(id={self._id_jugador!r}, nombre={self._nombre!r}, dorsal={self._dorsal!r} edad={self._edad!r}, posicion={self._posicion!r}, nacionalidad={self._nacionalidad!r})"
    
    def mostrar_informacion(self):
        print("-" * 30)  # Línea separadora
        print(f"ID: {self.id_jugador}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Dorsal: {self.dorsal}")
        print(f"Posición: {self.posicion}")
        print(f"Nacionalidad: {self.nacionalidad}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No disponible")
        print("-" * 30)  # Línea separadora

