from pathlib import Path

# Directorio raíz del proyecto (sube desde src/ al nivel del proyecto)
BASE_DIR: Path = Path(__file__).resolve().parent.parent
# Carpeta de datos dentro del proyecto
DATA_DIR: Path = BASE_DIR / "data"


def obtener_ruta_archivo(nombre_archivo: str) -> Path:
    """Devuelve la ruta absoluta al archivo dentro de la carpeta 'data'.

    Ejemplo: obtener_ruta_archivo('data.csv')
    """
    return DATA_DIR / nombre_archivo


__all__ = ["BASE_DIR", "DATA_DIR", "obtener_ruta_archivo"]
