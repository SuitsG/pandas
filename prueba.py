import functions.misFunctions as misFuncions
import src.path as path



# ========================================
""" Lectura de archivo CSV """
# ========================================
print("Archivo CSV 📁✅")
df_csv = path.obtener_ruta_archivo("data.csv")
df_csv = misFuncions.leer_csv(df_csv)
print(df_csv)


# ========================================
""" Lectura de archivos HTML """
# ========================================
print("\nArchivo HTML 📁✅")
url = "https://unite4buy.com/es/cpu/mobile-processors-ranking/"
df_html = misFuncions.leer_html(url)
print(df_html)

# ========================================
""" Lectura de archivos XLSX """
# ======================================== 
print("\nArchivo XLSX 📁✅")
df_xlsx = path.obtener_ruta_archivo("RELAX1.xlsx")
df_xlsx = misFuncions.leer_xlsx(df_xlsx)
print(df_xlsx)

# ========================================
""" Lectura de archivos JSON """
# ========================================
print("\nArchivo JSON 📁✅")
df_json = path.obtener_ruta_archivo("data.json")
df_json = misFuncions.leer_json(df_json)
print(df_json)



# ========================================
""" Lectura de un archivo csv desde una URL """
# ========================================
print("\nArchivo CSV desde URL 📁✅")
url_csv = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df_csv_url = misFuncions.leer_csv(url_csv)
print(df_csv_url)


# ==========================================
""" Creación de un DataFrame """
# ==========================================
print("\nCreación de un DataFrame 📁✅")
data = {
    "nombre": ["Juan", "Ana", "Luis"],
    "edad": [28, 24, 32],
    "sexo": ["Masculino", "Femenino", "Masculino"]
}

df_dataFrame = misFuncions.crear_dataframe(data)
print(df_dataFrame)


# ==========================================
# Imprimir los datos de la columna edad
# ==========================================
print("\nDatos de la columna 'edad' 📁✅")
print(df_dataFrame["edad"])