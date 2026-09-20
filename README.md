# ⚽ Futbolero - Sistema de Consulta de la Liga Argentina

Un sistema interactivo desarrollado en Python para consultar información sobre los equipos de la Primera División del Fútbol Argentino, sus estadios y sus planteles profesionales a partir de un archivo JSON.

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.x
* **Estructura de Datos:** JSON (Javascript Object Notation)
* **Librerías externas:** `pandas`, `openpyxl` (para el script de conversión)
* **Control de versiones:** Git & GitHub

---

## 📁 Estructura del Proyecto

FUTBOLERO/
│
├── equipos_argentina.xlsx     # Planilla editable de origen (Equipos y Jugadores)
├── equipos_argentina.json     # Base de datos en formato JSON
├── excel_a_json.py            # Script automatizado para convertir el Excel a JSON
├── Equipo.py                  # Clase que modela la entidad Equipo
├── Jugador.py                 # Clase que modela la entidad Jugador
├── Liga.py                    # Clase que gestiona la lista de equipos y búsquedas
└── main.py                    # Interfaz de usuario en terminal (Menú principal)

⚙️ Requisitos e Instalación
1. Clonar el repositorio:

git clone [https://github.com/jhonlezca/tp-Estructura-de-Datos.git](https://github.com/jhonlezca/tp-Estructura-de-Datos.git)

2. (Opcional) Instalar dependencias si necesitas regenerar el JSON desde el Excel:

pip install pandas openpyxl

🚀 Cómo Ejecutar el Programa

1. Abrí la terminal en la carpeta del proyecto en VS Code.

2. Ejecutá el archivo principal:

python main.py

3. Navegá por el menú interactivo para ingresar el nombre de tu equipo favorito o listar todos los clubes disponibles.

👨‍💻 Integrantes

- Fabricio y Jonatan