# Taller Python - Lectura de Archivos

Un proyecto simple para leer diferentes tipos de archivos usando Python y Pandas.

## 📁 Estructura del Proyecto

```
TallerPython/
├── data/                    # Archivos de datos
│   ├── data.csv
│   ├── data.json
│   └── RELAX*.xlsx
├── functions/
│   └── misFunctions.py      # Funciones para leer archivos
├── src/
│   └── path.py              # Utilidades para rutas
└── prueba.py                # Archivo principal de ejemplo
```

## 🚀 Uso

### Ejecutar el ejemplo completo:
```bash
python prueba.py
```

### Importar las funciones:
```python
import functions.misFunctions as misFuncions
import src.path as path

# Leer CSV
ruta_csv = path.obtener_ruta_archivo("data.csv")
datos_csv = misFuncions.leer_csv(ruta_csv)

# Leer JSON
ruta_json = path.obtener_ruta_archivo("data.json")
datos_json = misFuncions.leer_json(ruta_json)

# Leer Excel
ruta_xlsx = path.obtener_ruta_archivo("RELAX1.xlsx")
datos_xlsx = misFuncions.leer_xlsx(ruta_xlsx)

# Leer HTML desde URL
datos_html = misFuncions.leer_html("https://ejemplo.com")
```

## 📄 Tipos de Archivo Soportados

- **CSV**: Archivos de valores separados por comas
- **JSON**: Archivos de datos en formato JSON
- **Excel**: Archivos .xlsx
- **HTML**: Tablas desde páginas web

## 🛠️ Dependencias

- pandas
- openpyxl (para archivos Excel)
- lxml (para archivos HTML)

## 📝 Notas

- Las funciones manejan automáticamente diferentes codificaciones para archivos CSV
- Los archivos JSON con múltiples tablas muestran la primera tabla encontrada
- Todas las funciones devuelven las primeras 5 filas por defecto
