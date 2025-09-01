import pandas as pd



# ========================================
# Funcion para leer archivos CSV
# ========================================
def leer_csv(archivo):

    esquemaCodificacion = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']

    for codificacion in esquemaCodificacion:
        try:
            df_csv = pd.read_csv(archivo, encoding=codificacion)
            return df_csv.head().to_string()
        except (UnicodeDecodeError, ValueError):
            continue
    return "No se pudo leer el archivo CSV con ninguna de las codificaciones."


# ========================================
# Funcion para leer archivos HTML
# ========================================
def leer_html(url):
    df_html = pd.read_html(url)
    return df_html[0].head().to_string()


# ========================================
# Funcion para leer archivos XLSX
# ========================================
def leer_xlsx(archivo):
    df_xlsx = pd.read_excel(archivo)
    return df_xlsx.head().to_string()



# ========================================
# Funcion para leer archivos JSON
# ========================================
def leer_json(archivo):
    import json
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Si el JSON tiene múltiples claves, mostrar la primera tabla encontrada
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list) and len(value) > 0:
                df_json = pd.DataFrame(value)
                return f"Tabla: {key}\n" + df_json.head().to_string()
    
    # Si es una lista directa
    if isinstance(data, list):
        df_json = pd.DataFrame(data)
        return df_json.head().to_string()
    
    return str(data)


# ========================================
# Funcion para crear un DataFrame
# ========================================
def crear_dataframe(data):
    df = pd.DataFrame(data)
    return df