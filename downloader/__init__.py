"""
Paquete para descargar videos, playlist y audio desde Youtube con yt-dlp
"""


__version__ = "1.0.0" # version del proyecto

APP_DIR = Path.home() / "CuDownloader"

DEFAULT_DIR = str(APP_DIR)    # carpeta por defecto
HISTORY_FILE = str(APP_DIR / "has_downloaded.txt")  # registro de ya descargados
