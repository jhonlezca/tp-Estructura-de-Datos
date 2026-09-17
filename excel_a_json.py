import json
import pandas as pd

# 1. Cargar el archivo Excel
excel_path = "equipos_argentina.xlsx"

# Leer hojas
df_equipos = pd.read_excel(excel_path, sheet_name="Equipos")
df_jugadores = pd.read_excel(excel_path, sheet_name="Jugadores")

equipos_dict = {}

# Helper para limpiar campos vacíos o nulos
def limpiar_valor(val):
    if pd.isna(val) or str(val).strip() == "":
        return None
    return str(val).strip()

# Helper para valores numéricos opcionales
def limpiar_int(val):
    if pd.isna(val) or str(val).strip() == "":
        return None
    try:
        return int(val)
    except ValueError:
        return None

# 2. Procesar la información de Equipos
for _, fila in df_equipos.iterrows():
    id_eq = str(fila["id_equipo"]).strip()
    
    equipos_dict[id_eq] = {
        "id": id_eq,
        "nombre": limpiar_valor(fila.get("nombre")),
        "estadio": limpiar_valor(fila.get("estadio")),
        "zona": limpiar_valor(fila.get("zona")),
        "campeonato": {
            "posicion": limpiar_int(fila.get("pos_campeonato"))
        },
        "partidos": {
            "ultimo_partido": {
                "rival": limpiar_valor(fila.get("ult_rival")),
                "resultado": limpiar_valor(fila.get("ult_resultado")),
                "condicion": limpiar_valor(fila.get("ult_condicion"))
            },
            "siguiente_partido": {
                "rival": limpiar_valor(fila.get("sig_rival")),
                "condicion": limpiar_valor(fila.get("sig_condicion"))
            }
        },
        "plantel": []
    }

# 3. Procesar la información de Jugadores
for _, fila in df_jugadores.iterrows():
    id_eq = limpiar_valor(fila.get("id_equipo"))
    nombre = limpiar_valor(fila.get("nombre"))
    apellido = limpiar_valor(fila.get("apellido"))
    
    # Solo agregar el jugador si tiene datos mínimos (nombre o apellido)
    if id_eq in equipos_dict and (nombre or apellido):
        posicion = limpiar_valor(fila.get("posicion"))
        if posicion:
            posicion = posicion.capitalize()  # Estandariza Ej: 'defensor' -> 'Defensor'

        nacionalidad = limpiar_valor(fila.get("nacionalidad"))
        if nacionalidad:
            nacionalidad = nacionalidad.capitalize()

        jugador = {
            "id_jugador": limpiar_valor(fila.get("id_jugador")),
            "nombre": nombre,
            "apellido": apellido,
            "dorsal": limpiar_int(fila.get("dorsal")),
            "posicion": posicion,
            "nacionalidad": nacionalidad
        }
        equipos_dict[id_eq]["plantel"].append(jugador)

# 4. Estructura general final del JSON
json_final = {
    "metadatos": {
        "liga": "Liga Profesional de Fútbol",
        "pais": "Argentina",
        "temporada": 2026
    },
    "equipos": list(equipos_dict.values())
}

# 5. Guardar en el archivo JSON
with open("equipos_argentina.json", "w", encoding="utf-8") as f:
    json.dump(json_final, f, ensure_ascii=False, indent=2)

print("¡Archivo 'equipos_argentina.json' generado con éxito!")