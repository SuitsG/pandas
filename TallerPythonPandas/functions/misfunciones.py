#misfunciones.py
import pandas as pd
from pathlib import Path

# Configurar rutas
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "data"

def leer_datos(nombre_archivo):
    try:
        archivo_path = DATA_PATH / nombre_archivo
        if archivo_path.exists():
            # Intentar diferentes codificaciones
            codificaciones = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
            
            for encoding in codificaciones:
                try:
                    df = pd.read_csv(archivo_path, encoding=encoding)
                    print(f"✅ Archivo {nombre_archivo} cargado exitosamente con codificación {encoding}")
                    print(f"📊 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
                    return df
                except UnicodeDecodeError:
                    continue
            
            # Si ninguna codificación funciona, usar errors='ignore'
            df = pd.read_csv(archivo_path, encoding='utf-8', errors='ignore')
            print(f"✅ Archivo {nombre_archivo} cargado con manejo de errores")
            print(f"📊 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
            return df
        else:
            print(f"❌ Error: El archivo {nombre_archivo} no existe en {DATA_PATH}")
            return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {str(e)}")
        return None


def leer_html(url):
    try:
        tables = pd.read_html(url)
        if tables:
            print(f"✅ Página HTML cargada exitosamente")
            print(f"📊 Se encontraron {len(tables)} tabla(s)")
            return tables[0].head().to_string()  # Retorna la primera tabla
        else:
            print("❌ No se encontraron tablas en la URL")
            return None
    except Exception as e:
        print(f"❌ Error al leer HTML: {str(e)}")
        return None

def leer_xlsx(nombre_archivo):
    try:
        archivo_path = DATA_PATH / nombre_archivo
        if archivo_path.exists():
            df = pd.read_excel(archivo_path)
            print(f"✅ Archivo Excel {nombre_archivo} cargado exitosamente")
            print(f"📊 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
            return df
        else:
            print(f"❌ Error: El archivo {nombre_archivo} no existe en {DATA_PATH}")
            return None
    except Exception as e:
        print(f"❌ Error al leer el archivo Excel: {str(e)}")
        return None

def leer_json(nombre_archivo):
    try:
        archivo_path = DATA_PATH / nombre_archivo
        if archivo_path.exists():
            # Primero intentar leer como DataFrame directo
            try:
                df = pd.read_json(archivo_path)
                print(f"✅ Archivo JSON {nombre_archivo} cargado exitosamente")
                print(f"📊 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
                return df
            except:
                # Si falla, intentar leer como JSON y extraer arrays
                import json
                with open(archivo_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                # Si el JSON tiene una estructura anidada, buscar el primer array
                if isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, list):
                            df = pd.DataFrame(value)
                            print(f"✅ Archivo JSON {nombre_archivo} cargado desde clave '{key}'")
                            print(f"📊 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
                            return df
                
                # Si es un array directo
                elif isinstance(data, list):
                    df = pd.DataFrame(data)
                    print(f"✅ Archivo JSON {nombre_archivo} cargado exitosamente")
                    print(f"📊 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
                    return df
                
                print(f"❌ Error: El JSON no tiene una estructura compatible con DataFrame")
                return None
        else:
            print(f"❌ Error: El archivo {nombre_archivo} no existe en {DATA_PATH}")
            return None
    except Exception as e:
        print(f"❌ Error al leer el archivo JSON: {str(e)}")
        return None